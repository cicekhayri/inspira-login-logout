from inspira.auth.mixins.user_mixin import UserMixin
from sqlalchemy import Column, Integer, String
from database import Base


class User(Base, UserMixin):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
