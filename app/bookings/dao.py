from app.dao.base import BaseDAO
from app.database import async_session_maker

from sqlalchemy import select
from app.bookings.models import Bookings

class BookingDAO(BaseDAO):
    model = Bookings