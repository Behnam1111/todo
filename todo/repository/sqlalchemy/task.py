from typing import Dict, Any
from sqlalchemy.orm import Session
from todo.models.data.base_model import Task, Developer, Task_Developer


class TaskRepository:
    def __init__(self, sess: Session):
        self.sess: Session = sess

    def insert_task(self, task: Task) -> bool:
        try:
            self.sess.add(task)
            self.sess.commit()

        except:
            return False
        return True

    def update_task(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            self.sess.query(Task).filter(Task.id == id).update(details)
            self.sess.commit()

        except:
            return False
        return True

    def delete_task(self, id: int) -> bool:
        try:
            self.sess.query(Task).filter(Task.id == id).delete()
            self.sess.commit()

        except:
            return False
        return True

    def get_all_task(self):
        return self.sess.query(Task).all()

    def get_task(self, id: int):
        return self.sess.query(Task).filter(Task.id == id).one_or_none()

    def get_project_task(self, project_id: int):
        return self.sess.query(Task).filter(Task.project_id == project_id).all()

    def get_user_task_in_project(self, project_id: int, developer_id):
        result = self.sess.query(Task, Task_Developer).filter(Task.project_id == project_id).join(Task_Developer).\
            filter(Task.id == Task_Developer.task_id).filter(Task_Developer.developer_id == developer_id).all()
        return result