import shutil
from typing import Annotated

from fastapi import APIRouter, Depends, Query, UploadFile

from app.exceptions import PermissionDenied
from app.tasks.tasks import create_thumbnails
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(prefix="/images", tags=["Загрузка картинок"])


@router.post("/hotels")
def add_hotel_image(
    hotel_id: Annotated[int, Query(ge=0, le=1_000_000)],
    file: UploadFile,
    user: Users = Depends(get_current_user),
):
    if not user.is_admin:
        raise PermissionDenied
    image_path = f"app/static/images/{hotel_id}.webp"
    with open(image_path, "wb") as file_object:
        shutil.copyfileobj(file.file, file_object)
    create_thumbnails.delay(image_path)
