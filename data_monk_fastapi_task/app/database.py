from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv

load_dotenv()

DATABSE_URL = "sqlite:///./skilshare.db"

engine = create_engine(DATABSE_URL,echo = True)

def create_db():
    """create the database based on the models.py
    """
    SQLModel.metadata.create_all(engine)
    
def get_session():
    """get the session make sure that the no session cut 
    """
    with Session(engine) as session:
        yield session
