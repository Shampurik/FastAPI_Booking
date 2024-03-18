import shutil
from typing import Annotated

from fastapi import APIRouter, Query, UploadFile

from app.tasks.tasks import create_thumbnails

router = APIRouter(prefix="/images", tags=["Загрузка картинок"])


@router.post("/hotels")
def add_hotel_image(
    hotel_id: Annotated[int, Query(ge=0, le=1_000_000)], file: UploadFile
):
    image_path = f"app/static/images/{hotel_id}.webp"
    with open(image_path, "wb") as file_object:
        shutil.copyfileobj(file.file, file_object)
    create_thumbnails.delay(image_path)
