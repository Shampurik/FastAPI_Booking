from fastapi import FastAPI, Query
from datetime import date
from pydantic import BaseModel

from app.bookings.router import router as router_bookings
from app.users.router import router as router_users

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)


class SHotels(BaseModel):
    address: str
    name: str
    stars: int
    has_spa: bool


@app.get("/hotels")
def get_hotels(
    location: str,
    date_from: date,
    date_to: date,
    stars: int | None = Query(None, ge=1, le=5),
    has_spa: bool | None = None,
) -> list[SHotels]:
    hotel = {
        "address": "улица Валдай, морозильник 13",
        "name": "Владимир",
        "stars": 5,
        "has_spa": True,
        "lox": "loxs",
    }
    return [hotel]


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")
def add_booking(booking: SBooking):
    pass
