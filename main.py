from fastapi import FastAPI
from src.utils.dc import Base, engine
from src.tasks.models import TaskModel

Base.metadata.create_all(engine)


app=FastAPI(title="This is my Task Management Application")

# Posting the management task, updating the task/task progress, deleting the task when completed, real time track on the assets/time.

# Work on a AI based management recommendation system.
