from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    environment: str = "dev"
    unlimited_token: Optional[str] = None
    sentry_dsn: Optional[str] = None

    class Config:
        env_file = ".env"


CONFIG = Settings()
