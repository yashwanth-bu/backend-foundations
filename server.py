# server file

from fastapi import FastAPI
from task.routers import router as tasks_router
from task.database import Base, engine

# create FastAPI instance
server = FastAPI(
    title="Task-CRUD",
    version="0.1.0"
)

# initiating Base with database
Base.metadata.create_all(bind=engine)

# tasks router
server.include_router(tasks_router)

# health end point
@server.get("/health")
def check_health():
    return {
        "Status": "OK"
    }