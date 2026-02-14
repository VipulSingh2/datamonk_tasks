# here i define the structure of the database tables like the user and the skill model
from pydantic import EmailStr
from sqlalchemy import table
from sqlmodel import SQLModel, Field
from typing import Optional


class User(SQLModel,table = True):
    """table structure of the User
    """
    id :Optional[int] = Field(default=None,primary_key=True)
    username: str
    email: EmailStr
    password: str
    
class Skill(SQLModel,table = True):
    """table structure of the skill
    """
    id: Optional[int] = Field(default=None,primary_key=True)
    name:str
    level: str
    certificate: Optional[str] = None
    user_id: int = Field(foreign_key="user.id")