import enum                     #Built-in Python module for creating enumerations
from sqlalchemy import Column, Integer, String, Boolean, Enum, DateTime   #SQLAlchemy's column types
from sqlalchemy.sql import func        #This gives us SQL functions
from app.database import Base         #Imports the Base class we created in database.py

class UserRole(enum.Enum):             #Restricts the role column to only 3 valid values
    admin = "admin"
    standard = "standard"
    premium = "premium"

class User(Base):            #This inherits from Base telling SQLAlchemy its a database table
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)              #Primary Key
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.standard, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())