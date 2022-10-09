from pydantic import BaseModel


class TaskDeveloperReq(BaseModel):
    task_id: int
    developer_id: int

    class Config:
        orm_mode = True
