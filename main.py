from fastapi import FastAPI

from todo.api import login, signup, developer, task, project_manager

app = FastAPI()
app.include_router(signup.router, prefix='/todo')
app.include_router(login.router, prefix='/todo')
app.include_router(developer.router, prefix='/todo')
app.include_router(task.router, prefix='/todo')
app.include_router(project_manager.router, prefix='/todo')
