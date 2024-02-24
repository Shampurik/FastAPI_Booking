from fastapi import APIRouter

from app.hotels.dao import HotelDAO
from app.hotels.schemas import SHotelsInfo

router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("/find_by_location/{location}")
async def get_hotels_by_location(location: str) -> list[SHotelsInfo]:
    """Get hotels by location"""
    hotels = await HotelDAO.find_hotels_by_location(location)
    return hotels


@router.get("/all")
async def get_all_hotels() -> list[SHotelsInfo]:
    """Get all hotels."""
    hotels = await HotelDAO.find_all()
    return hotels


@router.get("/find_by_id/{hotel_id}")
async def get_hotel_by_id(hotel_id: int) -> SHotelsInfo:
    """Get hotel by id."""
    hotel = await HotelDAO.find_one_or_none(id=hotel_id)
    return hotel
