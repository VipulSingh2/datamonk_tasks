from time import timezone
import jwt
from datetime import datetime, timedelta,timezone
from dotenv import load_dotenv

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(hours = 1)
    
    to_encode.update({"exp":expire})
    
    return jwt.encode(to_encode)