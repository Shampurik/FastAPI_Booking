from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DbSettings(BaseSettings):
    DB_HOST: str = Field("localhost", env="DB_HOST")
    DB_PORT: int = Field(5432, env="DB_PORT")
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    REDIS_HOST: str = Field("localhost", env="REDIS_HOST")
    REDIS_PORT: int = Field(6379, env="REDIS_PORT")


class Settings(DbSettings):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

    START_MODE: Literal["DEV", "TEST", "PROD"] = Field("DEV")

    SMTP_HOST: str
    SMTP_PORT: str = Field(465, env="SMTP_PORT")
    SMTP_USER_EMAIL: str
    SMTP_PASS: str

    AUTH_KEY: str
    AUTH_ALGORITHM: str

    EXPIRE_CACHE: int = Field(60 * 5)


settings = Settings()
