from beanie import Document
from pydantic import BaseModel, EmailStr


class Admin(Document):
    full_name: str
    email: EmailStr

    class Settings:
        name = "admin"

    class Config:
        schema_extra = {
            "example": {
                "full_name": "Daniil Kimstach",
                "email": "daniilkimstachp@gmail.com"
            }
        }
