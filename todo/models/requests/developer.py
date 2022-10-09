from pydantic import BaseModel


class DeveloperReq(BaseModel):
    firstname: str
    lastname: str

    class Config:
        orm_mode = True
