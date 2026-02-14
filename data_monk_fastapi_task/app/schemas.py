from click import Option
from pydantic import BaseModel,EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    
class UserLogin(BaseModel):
    # identifier: str
    email: EmailStr
    password: str
    
    
class SkillCreate(BaseModel):
    name: str
    level: str
    
class SkillOut(BaseModel):
    id: int
    name: str
    level: str
    certificate: Optional[str]