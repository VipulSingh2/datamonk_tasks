from pydantic import BaseModel,Field
from typing import Annotated


class TaskSchema(BaseModel):
    title:Annotated[str,Field(...,description="Add the task title here",title="task title here")]
    description:str
    is_completed:bool=False
    
    
    
class TaskResponseSchema(BaseModel):
    id:int
    title:Annotated[str,Field(...,description="Add the task title here",title="task title here")]
    description:str
    is_completed:bool=False
