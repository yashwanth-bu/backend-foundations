from pydantic import BaseModel
from datetime import datetime

# by default pydantic expects data more like a dictionary
# models helps in validating data

# validate creating input data
class TaskCreate(BaseModel):
    title: str
    description: str | None = None

# validate updating input data
class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None

# validate the response model
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool
    created_at: datetime
    updated_at: datetime | None

    # helps to read python objects which default expects dictionary
    # sqlalchemy return the data from database in object then dictionary
    class Config:
        from_attributes = True
