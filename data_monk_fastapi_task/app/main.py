# this is the file where all the api and the routers are included to run my whole app like the authenticaion and the skills router to add and also add the endpoints here
from fastapi import FastAPI
from database import create_db
from routes.auth_routes import router as auth_router
from routes.skill_routes import router as skill_router
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespanner(app: FastAPI):
    create_db()
    print("tables are created")
    yield
    print("tables are closing")
app = FastAPI(title="SkillShare API",lifespan=lifespanner)

# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()



app.include_router(auth_router)
app.include_router(skill_router)
