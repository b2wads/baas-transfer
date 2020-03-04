import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    ACCOUNT_SERVICE_ADDRESS: str

    class Config:
        env_prefix = os.getenv("ENV", "SAQUE") + "_"


settings = Settings()
