from pydantic import BaseModel


class TaskReq(BaseModel):
    title: str
    description: str
    project_id: int

    class Config:
        orm_mode = True
