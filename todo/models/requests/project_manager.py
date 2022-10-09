from pydantic import BaseModel


class ProjectManagerReq(BaseModel):
    firstname: str
    lastname: str

    class Config:
        orm_mode = True
