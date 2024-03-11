from fastapi import APIRouter
from fastapi_cache.decorator import cache

from app.exceptions import NotFound
from app.hotels.dao import HotelDAO
from app.hotels.schemas import SHotelsInfo

router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("/find_by_location/{location}")
@cache(expire=30)
async def get_hotels_by_location(location: str) -> list[SHotelsInfo]:
    """Get hotels by location."""
    hotels = await HotelDAO.find_hotels_by_location(location)
    if not hotels:
        raise NotFound
    return hotels


@router.get("/all")
@cache(expire=30)
async def get_all_hotels() -> list[SHotelsInfo]:
    """Get all hotels."""
    hotels = await HotelDAO.find_all()
    return hotels


@router.get("/find_by_id/{hotel_id}")
@cache(expire=30)
async def get_hotel_by_id(hotel_id: int) -> SHotelsInfo:
    """Get hotel by id."""
    hotel = await HotelDAO.find_one_or_none(id=hotel_id)
    if not hotel:
        raise NotFound
    return hotel
