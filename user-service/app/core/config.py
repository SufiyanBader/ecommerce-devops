from pydantic_settings import BaseSettings
from pathlib import Path

# Always find .env relative to this file's location
ENV_FILE = Path(__file__).resolve().parent.parent.parent / ".env"

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/userdb"
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SERVICE_NAME: str = "user-service"
    VERSION: str = "1.0.0"

    class Config:
        env_file = str(ENV_FILE)

settings = Settings()