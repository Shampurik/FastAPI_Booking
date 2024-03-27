from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

if settings.START_MODE == "TEST":
    DB_HOST = settings.TEST_DB_HOST
    DB_PORT = settings.TEST_DB_PORT
    DB_USER = settings.TEST_DB_USER
    DB_PASS = settings.TEST_DB_PASS
    DB_NAME = settings.TEST_DB_NAME

    DB_PARAMS = {"poolclass": NullPool}
else:
    DB_HOST = settings.DB_HOST
    DB_PORT = settings.DB_PORT
    DB_USER = settings.DB_USER
    DB_PASS = settings.DB_PASS
    DB_NAME = settings.DB_NAME

    DB_PARAMS = {}

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(DATABASE_URL, **DB_PARAMS)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
