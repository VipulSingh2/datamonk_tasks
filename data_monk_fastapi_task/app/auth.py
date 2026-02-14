from passlib.context import CryptContext
from sqlmodel import Session, select
from models import User

# passlib = password security
# jwt = login session/identity proof

pwd_context = CryptContext(schemes=["bcrypt"],deprecated = "auto")

def hash_password(password: str):
    """converts the password in hash
    """
    return pwd_context.hash(password)

def verify_password(plain,hashed):
    """return the value in true/false as it mathches or not
    """
    return pwd_context.verify(plain,hashed)

def authenticate_user(email:str,password:str,session: Session):
    user = session.exec(select(User).where(User.email == email)).first()
    
    if not user:
        return None
    if not verify_password(password,user.password):
        return None
    return user