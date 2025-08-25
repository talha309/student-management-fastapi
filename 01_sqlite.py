from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import Base, SessionLocal, engine
from models import User, StudentForm as StudentFormModel
from pydantic_models import StudentForm, StudentResponse
from typing import List

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Registration API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Student Registration API is running!"}

@app.post("/students/", response_model=StudentResponse)
async def create_student(student: StudentForm, db: Session = Depends(get_db)):
    try:
        # Check if email already exists
        existing_email = db.query(StudentFormModel).filter(StudentFormModel.email == student.email).first()
        if existing_email:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        # Check if CNIC already exists
        existing_cnic = db.query(StudentFormModel).filter(StudentFormModel.cnic == student.cnic).first()
        if existing_cnic:
            raise HTTPException(status_code=400, detail="CNIC already registered")
        
        # Create new student
        db_student = StudentFormModel(**student.dict())
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student
    except HTTPException:
        db.rollback()
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.get("/students/", response_model=List[StudentResponse])
async def get_students(db: Session = Depends(get_db)):
    try:
        students = db.query(StudentFormModel).all()
        return students
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.get("/students/{student_id}", response_model=StudentResponse)
async def get_student(student_id: int, db: Session = Depends(get_db)):
    try:
        student = db.query(StudentFormModel).filter(StudentFormModel.id == student_id).first()
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        return student
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")