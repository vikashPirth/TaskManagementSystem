from fastapi import APIRouter

from db.database import SessionLocal
from db.models import Task

router = APIRouter()


@router.post("/tasks/")
def create_task(title: str, status: str, description: str = None):
    db = SessionLocal()
    task = Task(title=title, description=description, status=status)
    db.add(task)
    db.commit()
    db.refresh(task)
    db.close()
    return task
