from fastapi import FastAPI

app = FastAPI()

tasks = []

@app.get("/")
def home():
    return {"message": "Todo API is running!"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: dict):
    task["id"] = len(tasks) + 1
    tasks.append(task)
    return task

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return {"error": "Task not found"}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: dict):
    for task in tasks:
        if task["id"] == task_id:
            task.update(updated_task)
            task["id"] = task_id
            return task
    return {"error": "Task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}
    return {"error": "Task not found"}