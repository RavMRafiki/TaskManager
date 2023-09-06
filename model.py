from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base  = declarative_base()

class Task(Base):
    __tablename__ = "task"		
    id = Column(Integer, primary_key=True, index=True)		
    task_name = Column(String(20))		
    task_des = Column(String())		
    created_by = Column(String(20))
    date_created = Column(String())