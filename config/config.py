from typing import Optional
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings
from models.admin import Admin
from models.student import Student


class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    secret_key: str
    algorithm: str = "HS256"

    class Config:
        env_file = ".env.dev"
        orm_mode = True


async def initiate_database():
    client = AsyncIOMotorClient("mongodb://mongodb:27017/lms")
    await init_beanie(database=client.get_default_database(), document_models=[Admin, Student])