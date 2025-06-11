from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app=FastAPI()

class Task(BaseModel):
    id:int
    description:str
    done:bool=False

tasks_db=[]

@app.post("/tasks/",response_model=Task)
async def add_task(task:Task):
    tasks_db.append(task)
    return task

@app.get("/tasks/",response_model=List[Task])
async def get_tasks():
    return tasks_db

@app.put("/tasks/{tasks_id}",response_model=Task)
async def update_task(task_id:int,task:Task):
    for idx, existing_task in enumerate(tasks_db):
        if existing_task.id==task_id:
            tasks_db[idx]=task
            return task
    raise HTTPException(status_code=404,detail="Task not found")

@app.delete("/tasks/{task_id}",response_model=Task)
async def delete_task(task_id:int):
    for idx,existing_task in enumerate(tasks_db):
        if existing_task.id==task_id:
            delete_task=tasks_db.pop(idx)
            return delete_task
    raise HTTPException(status_code=404,detail="Task not found")
