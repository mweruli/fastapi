from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.user import User, UserCreate, UserResponse, UserBase
from settings import Settings
from routers.utils.user import get_user, get_user_by_email, get_users, create_user, get_user_by_name
from fastapi.encoders import jsonable_encoder
import secrets
from routers.utils.send_mail import send_registration_email


router = APIRouter(
    tags=["Users"]
)

@router.get("/users", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users



@router.post("/users")
async def create_new_user(user:UserCreate, db: Session = Depends(get_db)):
    username_found = get_user_by_name(db, username=user.username)
    email_found = get_user_by_email(db, email=user.email)

    if username_found:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Username already taken")
    if email_found:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Email already taken")

    await send_registration_email("Registration Successful", user.email, {
        "title": "Registration Sucessful",
        "name": user.username
    })
    
    return create_user(db=db, user=user)



@router.get("/users/{user_id}")
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"User not found")
    return db_user

