from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from todo.db_config.base_config import sess_db
from todo.models.data.base_model import Signup
from todo.models.requests.signup import SignupReq
from todo.repository.sqlalchemy.signup import SignupRepository

router = APIRouter()


@router.post("/signup/add")
def add_signup(req: SignupReq,
               sess: Session = Depends(sess_db)):
    repo: SignupRepository = SignupRepository(sess)
    signup = Signup(password=req.password, username=req.username, user_type=req.user_type)
    result = repo.insert_signup(signup)
    if result == True:
        return signup
    else:
        return JSONResponse(content={'message': 'create signup problem encountered'}, status_code=500)
