from collections import UserList
import email
from email.policy import default
from enum import unique
from msilib.schema import Class
from operator import index
import string
from sqlalchemy import Column, Boolean, String, Text, Enum, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
from db.database import Base
from db.models.mixins import Timestap
import enum


class Role(enum.IntEnum):
    Admin = 1
    Supervisor = 2
    Employee = 3

class User(Timestap, Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    role = Column(Enum(Role))
    is_active = Column(Boolean, default=False)
    password = Column(String(300), nullable=False)
    apikey =  Column(String(300), nullable=True)
    profile = relationship("Profile", back_populates= "owner", uselist=False)

class Profile(Base):
    __tablename__="profiles"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    bio = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="profile")

    # op.add_column(
    #     'users',
    #     sa.Column('role', sa.Enum('Admin', 'Supervisor', 'Employee', name='role'), nullable=True),
    # )