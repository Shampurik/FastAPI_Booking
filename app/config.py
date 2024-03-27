from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DbSettings(BaseSettings):
    DB_HOST: str = Field("localhost")
    DB_PORT: int = Field(5432)
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    TEST_DB_HOST: str
    TEST_DB_PORT: int
    TEST_DB_USER: str
    TEST_DB_PASS: str
    TEST_DB_NAME: str

    REDIS_HOST: str = Field("localhost")
    REDIS_PORT: int = Field(6379)


class Settings(DbSettings):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

    START_MODE: Literal["DEV", "TEST", "PROD"] = Field("DEV")

    SMTP_HOST: str
    SMTP_PORT: str = Field(465)
    SMTP_USER_EMAIL: str
    SMTP_PASS: str

    AUTH_KEY: str
    AUTH_ALGORITHM: str

    EXPIRE_CACHE: int = Field(60 * 5)


settings = Settings()
