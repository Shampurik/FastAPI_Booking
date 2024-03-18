from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    SMTP_HOST: str
    SMTP_PORT: str
    SMTP_USER_EMAIL: str
    SMTP_PASS: str

    AUTH_KEY: str
    AUTH_ALGORITHM: str

    class Config:
        env_file = ".env"


settings = Settings()
