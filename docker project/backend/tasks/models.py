from sqlalchemy import Column,String,Boolean,Integer
from utils.db import Base

class TaskModel(Base):
    __tablename__ = "models"
    """
    table banane ka tarika
    """
    id= Column(Integer,primary_key=True)
    title= Column(String)
    description = Column(String)
    is_completed = Column(Boolean)