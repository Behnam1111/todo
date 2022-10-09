from pydantic import BaseModel


class SignupReq(BaseModel):
    username: str
    password: str
    user_type: int

    class Config:
        orm_mode = True
