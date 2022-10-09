from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasicCredentials
from sqlalchemy.orm import Session

from todo.db_config.base_config import sess_db
from todo.repository.sqlalchemy.developer import DeveloperRepository
from todo.security.secure import http_basic

router = APIRouter()


@router.get("/developer/task/list")
async def list_task(project_id: int, developer_id: int, credentials: HTTPBasicCredentials = Depends(http_basic),
                    sess: Session = Depends(sess_db)):
    repo: DeveloperRepository = DeveloperRepository(sess)
    result = repo.get_user_task_in_project(project_id, developer_id)
    return result
