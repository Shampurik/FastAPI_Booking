from datetime import date

from fastapi import APIRouter, Depends, Response
from pydantic import TypeAdapter

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
from app.tasks.tasks import send_booking_confirmation_email
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
    return await BookingDAO.find_all(user_id=user.id)


@router.post("/add")
async def add_booking(
    room_id: int,
    date_from: date,
    date_to: date,
    user: Users = Depends(get_current_user),
):
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
    booking_dict = TypeAdapter(SBooking).validate_python(booking).model_dump()
    send_booking_confirmation_email.delay(booking_dict, user.email)
    return booking_dict


@router.delete("/{booking_id}")
async def delete_booking(
    response: Response,
    booking_id: int,
    user: Users = Depends(get_current_user),
):
    """Deletes booking for user"""
    await BookingDAO.delete_booking_for_user(
        booking_id=int(booking_id), user_id=user.id
    )
    response.status_code = 204
    return {"delete": "ok"}
