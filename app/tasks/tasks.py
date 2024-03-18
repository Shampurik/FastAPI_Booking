import smtplib
from pathlib import Path

from PIL import Image
from pydantic import EmailStr

from app.config import settings
from app.tasks.celery import celery
from app.tasks.email_templates import create_booking_confirmation_template


@celery.task
def create_thumbnails(
    path: str,
):
    image_path = Path(path)
    with Image.open(image_path) as image:
        resized_normal_image = image.copy()
        resized_small_image = image.copy()

        resized_normal_image.thumbnail((512, 512))
        resized_small_image.thumbnail((256, 256))

        resized_normal_image.save(f"app/static/images/normal_image{image_path.name}")
        resized_small_image.save(f"app/static/images/small_image{image_path.name}")


@celery.task
def send_booking_confirmation_email(booking: dict, email_to: EmailStr):
    email_to_mock = settings.SMTP_USER_EMAIL
    message_content = create_booking_confirmation_template(booking, email_to_mock)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER_EMAIL, settings.SMTP_PASS)
        server.send_message(message_content)
