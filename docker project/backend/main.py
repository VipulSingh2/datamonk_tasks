from fastapi import FastAPI
from tasks.router import task_routes
from utils.db import Base,engine

Base.metadata.create_all(bind = engine)

app = FastAPI(title="Basic crud Application",
              description="API for managing tasks",
              version="1.0.0",)


app.include_router(
    task_routes,
    # prefix="/tasks",
    tags=["Tasks"],)