from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from . import crud, schemas, database

app = FastAPI(title="Task Manager - Simple API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

database.create_tables()

@app.get("/tasks")
def list_tasks():
    return crud.get_tasks()

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = crud.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/tasks")
def add_task(task: schemas.TaskCreate):
    new_task = crud.create_task(task.title, task.description)
    return new_task

@app.put("/tasks/{task_id}")
def edit_task(task_id: int, task: schemas.TaskUpdate):
    existing = crud.get_task_by_id(task_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Task not found")
    crud.update_task(
        task_id,
        task.title or existing["title"],
        task.description or existing["description"],
        task.status or existing["status"]
    )
    updated = crud.get_task_by_id(task_id)
    return updated

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    existing = crud.get_task_by_id(task_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Task not found")
    crud.delete_task(task_id)
    return {"message": "Tarefa removida com sucesso"}
