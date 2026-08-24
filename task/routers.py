from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import get_db
from .schemas import TaskCreate, TaskUpdate, TaskResponse
from . import controllers


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


# CREATE
@router.post("/", response_model=TaskResponse)
def create_task(
    task_data: TaskCreate,
    db: Session = Depends(get_db)
):
    return controllers.create_task(db, task_data)


# READ ALL
@router.get("/", response_model=list[TaskResponse])
def get_tasks(
    db: Session = Depends(get_db)
):
    return controllers.get_tasks(db)


# READ ONE
@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    db: Session = Depends(get_db)
):

    task = controllers.get_task(db, task_id)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


# UPDATE
@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_data: TaskUpdate,
    db: Session = Depends(get_db)
):

    task = controllers.update_task(
        db,
        task_id,
        task_data
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


# DELETE
@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):

    task = controllers.delete_task(db, task_id)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task deleted successfully"
    }
