
from sqlalchemy.orm import Session
from db.models.user import User
from schemas.user import UserCreate
from routers.utils.hash import Hash
import secrets

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_name(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()



def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email, role=user.role, username=user.username, password=Hash.bcrypt(user.password), apikey = secrets.token_hex(30))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user