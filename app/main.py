import imp
from typing import Union

from fastapi import FastAPI
from app.routers import users
from app.db.database import engine
# from db.models import user
from app.db.models import user

user.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
