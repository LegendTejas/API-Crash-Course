from fastapi import FastAPI, Depends, HTTPException, Path
from auth import login_for_access_token, get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from models import Student, UpdateStudent
from typing import Optional

app = FastAPI(title="Student CRUD API with JWT Auth")

# In-memory student DB
students = {
    1: {"name": "John", "age": 18, "year": "1st year"}
}

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return login_for_access_token(form_data)

@app.get("/")
def index():
    return {"message": "Welcome to the Student API with JWT Authentication"}


# Read student by ID
@app.get("/students/{id}")
def get_student(
    id: int = Path(..., description="Student ID", gt=0),
    current_user: dict = Depends(get_current_user)
):
    student = students.get(id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


# Read student by name
@app.get("/students/by-name/")
def get_student_by_name(
    name: Optional[str] = None,
    current_user: dict = Depends(get_current_user)
):
    for student in students.values():
        if student["name"].lower() == name.lower():
            return student
    raise HTTPException(status_code=404, detail="Student not found")


# Create student
@app.post("/students/{id}")
def create_student(
    id: int,
    student: Student,
    current_user: dict = Depends(get_current_user)
):
    if id in students:
        raise HTTPException(status_code=400, detail="Student already exists")
    students[id] = student.model_dump()
    return {"message": "Student created successfully", "student": students[id]}


# Update student
@app.put("/students/{id}")
def update_student(
    id: int,
    student: UpdateStudent,
    current_user: dict = Depends(get_current_user)
):
    if id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    existing = students[id]
    if student.name: existing["name"] = student.name
    if student.age: existing["age"] = student.age
    if student.year: existing["year"] = student.year
    return {"message": "Student updated successfully", "student": existing}


# Delete student
@app.delete("/students/{id}")
def delete_student(
    id: int,
    current_user: dict = Depends(get_current_user)
):
    if id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    del students[id]
    return {"message": "Student deleted successfully"}