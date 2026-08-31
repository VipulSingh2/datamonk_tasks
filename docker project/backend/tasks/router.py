from fastapi import APIRouter,Depends,status
from tasks.models import TaskModel
from tasks.dtos import TaskSchema,TaskResponseSchema
from tasks import controller
from utils.db import get_db
from sqlalchemy.orm import Session
from typing import List

task_routes = APIRouter(prefix="/tasks")

@task_routes.post("/create",response_model=TaskResponseSchema,status_code= status.HTTP_201_CREATED)
def create_task(body: TaskSchema,db: Session=Depends(get_db)):
    return controller.create_task(body,db)

@task_routes.get("/all_tasks",response_model=List[TaskResponseSchema],status_code=status.HTTP_200_OK)
def get_task(db: Session=Depends(get_db)):
    return controller.get_task(db)

@task_routes.get("/one_task/{task_id}",response_model=TaskResponseSchema,status_code=status.HTTP_200_OK)
def get_one_task(task_id:int,db: Session=Depends(get_db)):
    return controller.get_one_task(task_id,db)


@task_routes.put("/update_task/{task_id}",status_code=status.HTTP_201_CREATED)
def update_task(body: TaskSchema,task_id:int,db: Session=Depends(get_db)):
    return controller.update_task(task_id,body,db)

@task_routes.delete("/delete_task/{task_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int,db: Session=Depends(get_db)):
    return controller.delete_task(task_id,db)