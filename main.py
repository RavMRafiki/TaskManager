from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from model import Task
from schema import task_schema
from session import create_get_session

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Server is up and running!"}

@app.get("/task", response_model=List[task_schema], status_code=200)
async def read_tasks(db: Session = Depends(create_get_session)):
   tasks = db.query(Task).all()
   return tasks

@app.post('/task', response_model = task_schema, status_code=201)
async def create_task(task: task_schema, db: Session = Depends(create_get_session)):
   new_task = Task(
        task_name = task.task_name,
        task_des = task.task_des,
        created_by =task.created_by,
        date_created = task.date_created,
   )
   db.add(new_task)
   db.commit()

   return new_task

@app.get("/task/{id}", response_model = task_schema, status_code=200)
async def get_task(id:int,db: Session = Depends(create_get_session)):
   task = db.query(Task).get(id)
   return task

@app.patch("/task/{id}", response_model = task_schema, status_code=200)
async def update_task(id:int, task:task_schema, db: Session = Depends(create_get_session)):
   db_task = db.query(Task).get(id)
   db_task.task_name = task.task_name
   db_task.task_des =  task.task_des
   db.commit()
   db.refresh(db_task)

   return db_task

@app.delete('/task/{id}', status_code=200)
async def delete_task(id: int, db: Session = Depends(create_get_session)):
    db_task = db.query(Task).get(id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task id does not exist")
    db.delete(db_task)
    db.commit()
    return None