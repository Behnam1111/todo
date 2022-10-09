from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasicCredentials
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from todo.db_config.base_config import sess_db
from todo.models.data.base_model import Task_Developer
from todo.models.requests.task_developer import TaskDeveloperReq
from todo.repository.sqlalchemy.login import LoginRepository
from todo.repository.sqlalchemy.task_developer import TaskDeveloperRepository
from todo.security.secure import http_basic

router = APIRouter()


@router.post("/project_manager/assign/task")
async def add_task(req: TaskDeveloperReq, credentials: HTTPBasicCredentials = Depends(http_basic),
                   sess: Session = Depends(sess_db)):
    loginrepo = LoginRepository(sess)
    account = loginrepo.get_all_login_username(credentials.username)
    if account.user_type != 2:
        return JSONResponse(content={'message': 'you do not have sufficient credentials'}, status_code=401)
    repo: TaskDeveloperRepository = TaskDeveloperRepository(sess)
    task_developer = Task_Developer(task_id=req.task_id, developer_id=req.developer_id)
    result = repo.insert_task_developer(task_developer)
    if result:
        return task_developer
    else:
        return JSONResponse(content={'message': 'create task problem encountered'}, status_code=500)
