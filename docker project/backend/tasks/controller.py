from tasks.dtos import TaskSchema,TaskResponseSchema
from tasks.models import TaskModel
from sqlalchemy.orm import Session

from fastapi import status,HTTPException

def create_task(body: TaskSchema,db: Session):
    data = body.model_dump()
    new_task = TaskModel(
    title = data.get("title"),
    description =data["description"],
    is_completed=data["is_completed"],
    )
    # print(new_task)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
    # print(new_task)
    # return {"status":"Task created successfully","data":new_task}

def get_task(db: Session):
    tasks:TaskResponseSchema = db.query(TaskModel).all()
    return tasks

def get_one_task(task_id:int,db: Session):
    one_task:TaskResponseSchema = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = "Task with the is is not present.")
    return one_task

def update_task(task_id:int,body,db: Session):
    one_task:TaskResponseSchema = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = "Task with the is is not present.")
    body = body.model_dump()
    for key,value in body.items():
        setattr(one_task,key,value)
    
    db.add(one_task)
    db.commit()
    db.refresh(one_task)
    return one_task

def delete_task(task_id:int,db:Session):
    one_task:TaskResponseSchema = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = "Task with the is is not present.")
    db.delete(one_task)
    db.commit()
    return None