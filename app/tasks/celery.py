from celery import Celery

celery = Celery("tasks", broker="redis://localhost", include=["app.tasks.tasks"])

# celery -A app.tasks.celery:celery worker --loglevel=INFO
