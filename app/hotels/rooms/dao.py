from datetime import date

from app.bookings.dao import BookingDAO
from app.dao.base import BaseDAO
from app.hotels.rooms.models import Rooms
from app.hotels.rooms.schemas import SRooms


class RoomsDAO(BaseDAO):
    model = Rooms

    @classmethod
    async def get_available_rooms_by_hotel_id(
        cls, hotel_id: int, date_from: date, date_to: date
    ):
        result: list = []
        # get all rooms by hotel id
        rooms: list[SRooms] = [
            room for room in await cls.find_all_filter(Rooms.hotel_id == hotel_id)
        ]
        # get all available rooms
        for room in rooms:
            rooms_qty = room.quantity
            rooms_booked: int = len(
                await BookingDAO.get_booking_rooms_by_id(room.id, date_from, date_to)
            )
            rooms_left: int = int(rooms_qty) - int(rooms_booked)
            if rooms_left:
                room.rooms_left = rooms_left
                result.append(room)
        return result
