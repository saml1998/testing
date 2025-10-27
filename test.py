# backend/app/settings.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_HOST: str = "localhost"         # Change if using Azure/Postgres Cloud
    DATABASE_PORT: int = 5432
    DATABASE_USER: str = "adminuser"         # Change to your Postgres username
    DATABASE_PASSWORD: str = "YourPassword"  # Replace with your actual password
    DATABASE_NAME: str = "postgres"          # Or your DB name (like opco_db)

    class Config:
        env_file = ".env"  # Allows loading from .env automatically

settings = Settings()


















