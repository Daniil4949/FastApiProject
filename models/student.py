from beanie import Document
from pydantic import BaseModel, EmailStr
from typing import Optional, Any


class Student(Document):
    full_name: str
    email: EmailStr
    course_of_study: str
    age: int
    average_grade: float

    class Config:
        schema_extra = {
            "example": {
                "full_name": "Denis Valuev",
                "email": "denis@gmail.com",
                "course_of_study": '2',
                "age": 19,
                "average_grade": 8.7
            }
        }


class UpdateStudentModel(BaseModel):
    full_name: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    age: Optional[int]
    average_grade: Optional[str]

    class Settings:
        name = "student"

    class Config:
        schema_extra = {
            "example":
                {
                    "full_name": "Denis Valuev",
                    "email": "denis@gmail.com",
                    "course_of_study": "2",
                    "age": 19,
                    "average_grade": 9.4
                }
        }


class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Sample data"
            }
        }
