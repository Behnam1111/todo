from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasicCredentials
from sqlalchemy.orm import Session

from todo.db_config.base_config import sess_db
from todo.repository.sqlalchemy.task import TaskRepository
from todo.security.secure import http_basic

router = APIRouter()


@router.get("/task/project/list")
async def list_task(project_id: int, credentials: HTTPBasicCredentials = Depends(http_basic),
                    sess: Session = Depends(sess_db)):
    repo: TaskRepository = TaskRepository(sess)
    result = repo.get_project_task(project_id)
    return result
