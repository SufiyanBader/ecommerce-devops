from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/productdb"
    SERVICE_NAME: str = "product-service"
    VERSION: str = "1.0.0"

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}

settings = Settings()