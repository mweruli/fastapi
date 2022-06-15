from datetime import datetime
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: int
    password: str

class UserCreate(UserBase):
    ...


class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True


class UserResponse(UserBase):
    id: int
    username: str
    email: EmailStr
    role: int
    
    
        