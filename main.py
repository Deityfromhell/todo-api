from fastapi import FastAPI, HTTPException

app = FastAPI()

tasks = [
    {"id": 1, "title": "Final sınavına çalış", "done": False},
    {"id": 2, "title": "FlyRank projesini tamamla", "done": False},
    {"id": 3, "title": "GitHub reposunu güncelle", "done": True}
]

@app.get("/")
def home():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.get("/tasks/{task_id}", summary="Get one task")
def health():
    return {"status": "ok"}

@app.get("/tasks", summary="List all tasks")
def get_tasks():
    return tasks

@app.post("/tasks", status_code=201, summary="Create a task")
def create_task(task: dict):
    if "title" not in task or not task["title"].strip():
        raise HTTPException(status_code=400, detail="Title is required")
    task["id"] = len(tasks) + 1
    task["done"] = False
    tasks.append(task)
    return task

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=400, detail=f"Task {task_id} not found")

@app.put("/tasks/{task_id}", summary="Update a task")
def update_task(task_id: int, updated_task: dict):
    if not updated_task:
        raise HTTPException(status_code=400, detail="Request body cannot be empty")

    if "title" in updated_task and not updated_task["title"].strip():
        raise HTTPException(status_code=400, detail="Title cannot be empty")

    for task in tasks:
        if task["id"] == task_id:
            task.update(updated_task)
            task["id"] = task_id
            return task

    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@app.delete("/tasks/{task_id}", status_code=204, summary="Delete a task")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")