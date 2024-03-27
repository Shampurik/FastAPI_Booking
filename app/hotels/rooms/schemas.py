from pydantic import BaseModel, ConfigDict


class SRooms(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    hotel_id: int
    name: str
    description: str | None
    price: int
    services: list[str]
    quantity: int
    image_id: int


class SRoomsLeft(SRooms):
    rooms_left: int
