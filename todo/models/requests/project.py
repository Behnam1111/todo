from pydantic import BaseModel


class ProjectReq(BaseModel):
    title: str
    project_manager: int

    class Config:
        orm_mode = True
