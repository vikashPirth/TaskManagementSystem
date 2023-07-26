# database.py
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.base import Base
from db.models import Task, User

SQLALCHEMY_DATABASE_URL = "postgresql://vikashpirthiani:your_password@localhost/task_management_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.DEBUG)

def create_tables():
    print(" I am done fucking")
    Base.metadata.create_all(bind=engine)
    print("done")


def drop_tables():
    Base.metadata.drop_all(bind=engine)
