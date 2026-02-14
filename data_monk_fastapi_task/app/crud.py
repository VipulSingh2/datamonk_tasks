from ssl import HAS_NEVER_CHECK_COMMON_NAME
from sqlmodel import Session, select
from models import User, Skill
from auth import hash_password

def create_user(user_data, session: Session):
    user = User(
        username = user_data.username,
        email = user_data.email,
        password= hash_password(user_data.password)
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def create_skill(skill_data,user_id,session: Session):
    skill= Skill(
        name = skill_data.name,
        level = skill_data.level,
        user_id = user_id
    )
    
    session.add(skill)
    session.commit()
    session.refresh(skill)
    return skill
    