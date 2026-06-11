from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import Optional
from datetime import datetime

class UserRole(str, Enum):
    admin = "admin"
    standard = "standard"
    premium = "premium"

# What we expect when someone registers
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: Optional[UserRole] = UserRole.standard

# What we return after registration or login (never the password)
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    role: UserRole
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

# What we expect when someone logs in
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# What we return after a successful login
class Token(BaseModel):
    access_token: str
    token_type: str