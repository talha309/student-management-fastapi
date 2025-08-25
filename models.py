from sqlalchemy import Column, Integer, String, Date
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)

class StudentForm(Base):
    __tablename__ = "student_form"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    cnic = Column(String(15), unique=True, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    phone_number = Column(String(11))
    address = Column(String(200))
    degree = Column(String(100), nullable=False)
    