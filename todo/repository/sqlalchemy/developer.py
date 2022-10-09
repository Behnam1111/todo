from typing import Dict, Any

from sqlalchemy.orm import Session

from todo.models.data.base_model import Task, Developer, Task_Developer


class DeveloperRepository:

    def __init__(self, sess: Session):
        self.sess: Session = sess

    def insert_developer(self, developer: Developer) -> bool:
        try:
            self.sess.add(developer)
            self.sess.commit()
        except:
            return False
        return True

    def update_developer(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            self.sess.query(Developer).filter(Developer.id == id).update(details)
            self.sess.commit()

        except:
            return False
        return True

    def delete_developer(self, id: int) -> bool:
        try:
            self.sess.query(Developer).filter(Developer.id == id).delete()
            self.sess.commit()

        except:
            return False
        return True

    def get_all_developer(self):
        return self.sess.query(Developer).all()

    def get_developer(self, id: int):
        return self.sess.query(Developer).filter(Developer.id == id).one_or_none()

    def get_user_task_in_project(self, project_id: int, developer_id):
        result = self.sess.query(Task, Task_Developer).filter(Task.project_id == project_id).join(Task_Developer). \
            filter(Task.id == Task_Developer.task_id).filter(Task_Developer.developer_id == developer_id).all()
        return result
