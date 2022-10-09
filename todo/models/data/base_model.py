from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from todo.db_config.base_config import Base
from todo.db_config.base_config import engine


class Signup(Base):
    __tablename__ = "signup"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column('username', String(45), unique=True, index=False)
    password = Column('password', String(45), unique=False, index=False)
    user_type = Column('user_type', Integer, unique=False, index=False)


class Login(Base):
    __tablename__ = "login"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(45), unique=False, index=False)
    password = Column(String(45), unique=False, index=False)
    passphrase = Column(String(200), unique=False, index=False)
    approved_date = Column(Date, unique=False, index=False)
    user_type = Column(Integer, unique=False, index=False)

    developers = relationship('Developer', back_populates="login", uselist=False)
    project_managers = relationship('ProjectManager', back_populates="login", uselist=False)


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(45), nullable=False)
    description = Column(String(45), nullable=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)

    projects = relationship('Project', back_populates="tasks", uselist=False)


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(45), nullable=False)

    tasks = relationship("Task", back_populates="projects")


class Developer(Base):
    __tablename__ = "developers"
    id = Column(Integer, ForeignKey('login.id'), primary_key=True, index=True, autoincrement=True)
    firstname = Column(String(45), unique=False, index=False)
    lastname = Column(String(45), unique=False, index=False)

    login = relationship('Login', back_populates="developers")


class ProjectManager(Base):
    __tablename__ = "project_managers"
    id = Column(Integer, ForeignKey('login.id'), primary_key=True, index=True, autoincrement=True)
    firstname = Column(String(45), unique=False, index=False)
    lastname = Column(String(45), unique=False, index=False)

    login = relationship('Login', back_populates="project_managers")
    is_manager_of = Column(Integer, ForeignKey("projects.id"))


class Task_Developer(Base):
    __tablename__ = "task_developer"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    task_id = Column(Integer, ForeignKey('tasks.id'), unique=False, index=False)
    developer_id = Column(Integer, ForeignKey('developers.id'), unique=False, index=False)


class Project_Developer(Base):
    __tablename__ = "project_developer"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('projects.id'), unique=False, index=False)
    developer_id = Column(Integer, ForeignKey('developers.id'), unique=False, index=False)


Base.metadata.create_all(engine)
