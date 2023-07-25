from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    status = Column(String, index=True, default="To Do")
    due_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    assignee_id = Column(Integer, ForeignKey('users.id'))

    assignee = relationship("User", back_populates="tasks")
