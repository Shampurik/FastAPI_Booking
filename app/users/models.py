from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_admin = Column(Boolean, server_default="FALSE", nullable=False)
    bookings = relationship("Bookings", back_populates="user")

    def __str__(self) -> str:
        return f"User {self.email}"
