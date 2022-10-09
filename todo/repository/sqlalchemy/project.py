from typing import Dict, Any
from sqlalchemy.orm import Session
from todo.models.data.base_model import Project


class ProjectRepository:

    def __init__(self, sess: Session):
        self.sess: Session = sess

    def insert_project(self, project: Project) -> bool:
        try:
            self.sess.add(project)
            self.sess.commit()
            print(project.id)
        except:
            return False
        return True

    def update_project(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            self.sess.query(Project).filter(Project.id == id).update(details)
            self.sess.commit()

        except:
            return False
        return True

    def delete_project(self, id: int) -> bool:
        try:
            self.sess.query(Project).filter(Project.id == id).delete()
            self.sess.commit()

        except:
            return False
        return True

    def get_all_project(self):
        return self.sess.query(Project).all()

    def get_project(self, id: int):
        return self.sess.query(Project).filter(Project.id == id).one_or_none()
