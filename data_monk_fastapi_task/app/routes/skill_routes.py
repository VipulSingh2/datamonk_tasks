from fastapi import APIRouter, Depends, UploadFile, File
from sqlmodel import Session
import os

from database import get_session
from schemas import SkillCreate
from crud import create_skill

router = APIRouter(prefix="/skills", tags=["Skills"])

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@router.post("/")
def add_skill(skill: SkillCreate, session: Session = Depends(get_session)):
    return create_skill(skill, user_id=1, session=session)   # temp user


@router.post("/upload/")
async def upload_certificate(file: UploadFile = File(...)):
    file_path = f"{UPLOAD_FOLDER}/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    return {"filename": file.filename}
