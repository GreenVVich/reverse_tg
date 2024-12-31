from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str
    LOGS_FILE: str

    class Config:
        env_file = ".env"


settings = Settings()