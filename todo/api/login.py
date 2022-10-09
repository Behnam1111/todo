from datetime import date

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasicCredentials
from sqlalchemy.orm import Session

from todo.db_config.base_config import sess_db
from todo.models.data.base_model import Login, Signup
from todo.repository.sqlalchemy.login import LoginRepository
from todo.repository.sqlalchemy.signup import SignupRepository
from todo.security.secure import http_basic, authenticate, get_password_hash

router = APIRouter()


@router.get("/approve/signup")
def signup_approve(username: str,
                   sess: Session = Depends(sess_db)):
    signuprepo = SignupRepository(sess)
    result: Signup = signuprepo.get_signup_username(username)
    if result == None:
        return JSONResponse(content={'message': 'username is not valid'}, status_code=401)
    else:
        passphrase = get_password_hash(result.password)
        login = Login(username=result.username, password=result.password, passphrase=passphrase,
                      approved_date=date.today(), user_type=result.user_type)
        loginrepo = LoginRepository(sess)
        success = loginrepo.insert_login(login)
        if success == False:
            return JSONResponse(content={'message': 'create login problem encountered'}, status_code=500)
        else:
            return login


@router.get("/login")
def login(credentials: HTTPBasicCredentials = Depends(http_basic), sess: Session = Depends(sess_db)):
    loginrepo = LoginRepository(sess)
    account = loginrepo.get_all_login_username(credentials.username)
    if authenticate(credentials, account) and not account == None:
        return account
    else:
        raise HTTPException(
            status_code=400, detail="Incorrect username or password")
