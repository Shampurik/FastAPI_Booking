from datetime import date

from fastapi import APIRouter
from fastapi_cache.decorator import cache

from app.config import settings
from app.hotels.rooms.dao import RoomsDAO
from app.hotels.rooms.schemas import SRoomsLeft

router = APIRouter(prefix="/hotels", tags=["Rooms"])


@router.get("/{hotel_id}/rooms")
@cache(expire=settings.EXPIRE_CACHE)
async def get_all_rooms_by_hotel_id(
    hotel_id: str, date_from: date, date_to: date
) -> list[SRoomsLeft]:
    """Returns all available rooms by hotel id between date_from - date_to."""
    return await RoomsDAO.get_available_rooms_by_hotel_id(
        int(hotel_id), date_from, date_to
    )
