from fastapi import APIRouter, Body, Request
from database.db import *
from models.student import *

router = APIRouter(
    prefix="/students",
    tags=["students"]
)


@router.get("/", response_description="Students retrieved", response_model=Response)
async def get_students(request: Request):
    students = await retrieve_students()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Students data  retrieved successfully",
        "data": students
    }


@router.get("/{id}", response_description="Student data retrieved", response_model=Response)
async def get_student_data(id: PydanticObjectId):
    student = await retrieve_student(id)
    if student:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Student data retrieved successfully",
            "data": student
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Student doesn't exist"
    }


@router.post("/", response_description="Student data added into the database", response_model=Response)
async def add_new_student(student: Student = Body(...)):
    new_student = await add_student(student)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Student created successfully",
        "data": new_student
    }


@router.delete("/{id}", response_description="Deleting student from database")
async def delete_student_data(id: PydanticObjectId):
    deleted_student = await delete_student(id)
    if deleted_student:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Student with ID: {} removed".format(id),
            "data": deleted_student
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Student with {} doesn't exist".format(id),
        "data": False
    }


@router.put("/{id}", response_model=Response)
async def update_student(id: PydanticObjectId, req: UpdateStudentModel = Body(...)):
    updated_student = await update_student_data(id, req.dict())
    if updated_student:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Student with ID: {} updated".format(id),
            "data": updated_student
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Student with ID {}: not found".format(id)
    }
