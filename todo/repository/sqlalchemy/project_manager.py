from typing import Dict, Any
from sqlalchemy.orm import Session
from todo.models.data.base_model import ProjectManager


class ProjectManagerRepository:

    def __init__(self, sess: Session):
        self.sess: Session = sess

    def insert_projectmanager(self, projectmanager: ProjectManager) -> bool:
        try:
            self.sess.add(projectmanager)
            self.sess.commit()
        except:
            return False
        return True

    def update_projectmanager(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            self.sess.query(ProjectManager).filter(ProjectManager.id == id).update(details)
            self.sess.commit()

        except:
            return False
        return True

    def delete_projectmanager(self, id: int) -> bool:
        try:
            signup = self.sess.query(ProjectManager).filter(ProjectManager.id == id).delete()
            self.sess.commit()

        except:
            return False
        return True

    def get_all_projectmanager(self):
        return self.sess.query(ProjectManager).all()

    def get_projectmanager(self, id: int):
        return self.sess.query(ProjectManager).filter(ProjectManager.id == id).one_or_none()
