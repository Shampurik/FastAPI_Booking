from datetime import date

from fastapi import APIRouter

from app.hotels.rooms.dao import RoomsDAO
from app.hotels.rooms.schemas import SRoomsLeft

router = APIRouter(prefix="/hotels", tags=["Rooms"])


@router.get("/{hotel_id}/rooms")
async def get_all_rooms_by_hotel_id(
    hotel_id: str, data_from: date, data_to: date
) -> list[SRoomsLeft]:
    """Returns all available rooms by hotel id between date_from - date_to."""
    return await RoomsDAO.get_available_rooms_by_hotel_id(
        int(hotel_id), data_from, data_to
    )
