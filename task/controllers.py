from sqlalchemy.orm import Session

from .models import Task
from .schemas import TaskCreate, TaskUpdate


# CREATE
def create_task(db: Session, task_data: TaskCreate):

    task = Task(
        title=task_data.title,
        description=task_data.description
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


# READ ALL
def get_tasks(db: Session):

    return db.query(Task).all()


# READ ONE
def get_task(db: Session, task_id: int):

    return db.query(Task).filter(Task.id == task_id).first()


# UPDATE
def update_task(
    db: Session,
    task_id: int,
    task_data: TaskUpdate
):

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        return None

    if task_data.title is not None:
        task.title = task_data.title

    if task_data.description is not None:
        task.description = task_data.description

    if task_data.completed is not None:
        task.completed = task_data.completed

    db.commit()
    db.refresh(task)

    return task


# DELETE
def delete_task(db: Session, task_id: int):

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        return None

    db.delete(task)
    db.commit()

    return task