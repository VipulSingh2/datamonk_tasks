from fastapi import APIRouter, Depends
from sqlmodel import Session
from schemas import UserCreate,UserLogin
from database import get_session
from crud import create_user
from auth import authenticate_user
from utils.jwt_handler import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(user:UserCreate,session: Session= Depends(get_session)):
    return create_user(user,session)

@router.post("/login")
def login(user: UserLogin, session: Session = Depends(get_session)):
    db_user = authenticate_user(user.email, user.password,session)
    
    if not db_user:
        return {"error":"Invalid credentials"}
    
    token = create_access_token({"sub":db_user.email})
    return {"access_token": token}