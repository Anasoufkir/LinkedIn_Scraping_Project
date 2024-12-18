
import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    API_KEY: str = os.getenv("API_KEY", "your_api_key")

settings = Settings()
