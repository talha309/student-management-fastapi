from pydantic import BaseModel, EmailStr, Field, validator
from datetime import date, datetime
from typing import Optional
import re

class StudentForm(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50, description="Student's first name")
    last_name: str = Field(..., min_length=1, max_length=50, description="Student's last name")
    email: EmailStr = Field(..., description="Student's email address")
    cnic: str = Field(..., description="Pakistani CNIC in format XXXXX-XXXXXXX-X")
    date_of_birth: date = Field(..., description="Date of birth in YYYY-MM-DD format")
    phone_number: Optional[str] = Field(None, description="Phone number in format 03XXXXXXXXX")
    address: Optional[str] = Field(None, max_length=200, description="Student's residential address")
    degree: str = Field(..., min_length=1, max_length=100, description="Degree or program name")

    @validator("cnic")
    def validate_cnic(cls, v):
        if not re.match(r"^\d{5}-\d{7}-\d{1}$", v):
            raise ValueError("CNIC must be in the format XXXXX-XXXXXXX-X (e.g., 33100-2234567-1)")
        return v

    @validator("phone_number")
    def validate_phone_number(cls, v):
        if v is None:
            return v
        if not re.match(r"^03\d{9}$", v):
            raise ValueError("Phone number must be in the format 03XXXXXXXXX (e.g., 03001234567)")
        return v

    @validator("date_of_birth")
    def validate_date_of_birth(cls, v):
        today = datetime(2025, 8, 24).date()
        age_years = (today - v).days // 365
        if not (15 <= age_years <= 100):
            raise ValueError("Student must be between 15 and 100 years old")
        return v

class StudentResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    cnic: str
    date_of_birth: date
    phone_number: Optional[str]
    address: Optional[str]
    degree: str

    class Config:
        orm_mode = True