from typing import Dict, Any
from sqlalchemy.orm import Session

from todo.models.data.base_model import Task_Developer


class TaskDeveloperRepository:
    def __init__(self, sess: Session):
        self.sess: Session = sess

    def insert_task_developer(self, task_developer: Task_Developer) -> bool:
        try:
            self.sess.add(task_developer)
            self.sess.commit()

        except:
            return False
        return True

    def update_task_developer(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            self.sess.query(Task_Developer).filter(Task_Developer.id == id).update(details)
            self.sess.commit()

        except:
            return False
        return True

    def delete_task_developer(self, id: int) -> bool:
        try:
            self.sess.query(Task_Developer).filter(Task_Developer.id == id).delete()
            self.sess.commit()

        except:
            return False
        return True

    def get_all_task_developer(self):
        return self.sess.query(Task_Developer).all()
