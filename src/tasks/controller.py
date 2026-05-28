from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session

def create_task(body:TaskSchema, db:Session):
    data = body.model_dump()
    

    return {"status":"Task Created Successfully!"}