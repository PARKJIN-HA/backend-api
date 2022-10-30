import uuid

from sqlalchemy.orm import Session

import models
import schemas


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(UUID=uuid.uuid4() ,Email=user.Email, PW=user.PW, Name=user.Name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: str):
    db.query(models.User).filter(models.User.UUID == user_id).delete()
    db.commit()

def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.UUID == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.Email == email).first()

def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.Name == name).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_schedule(db: Session, schedule: schemas.ScheduleCreate):
    db_schedule = models.Schedule(**schedule.dict())
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule

def delete_schedule(db: Session, schedule_id: str):
    db.query(models.Schedule).filter(models.Schedule.UUID == schedule_id).delete()
    db.commit()

def get_schedules(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Schedule).offset(skip).limit(limit).all()

def get_schedule(db: Session, schedule_id: str):
    return db.query(models.Schedule).filter(models.Schedule.UUID == schedule_id).first()

def get_schedule_by_owner(db: Session, owner: str):
    return db.query(models.Schedule).filter(models.Schedule.Owner == owner).first()

def get_schedule_by_member(db: Session, member: str):
    return db.query(models.Schedule).filter(models.Schedule.Members == member).first()


def create_details(db: Session, details: schemas.DetailsCreate):
    db_details = models.Details(**details.dict())
    db.add(db_details)
    db.commit()
    db.refresh(db_details)
    return db_details

def delete_details(db: Session, details_id: str):
    db.query(models.Details).filter(models.Details.UUID == details_id).delete()
    db.commit()

def get_details(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Details).offset(skip).limit(limit).all()

def get_details_by_schedule_id(db: Session, schedule_id: str):
    return db.query(models.Details).filter(models.Details.ScheduleUUID == schedule_id).all()


def create_schedule_details(db: Session, schedule_id: str, details_id: str):
    db_details = models.Details(UUID=details_id, ScheduleUUID=schedule_id)
    db.add(db_details)
    db.commit()
    db.refresh(db_details)
    return db_details

def delete_details_by_schedule_id(db: Session, schedule_id: str):
    db.query(models.Details).filter(models.Details.ScheduleUUID == schedule_id).delete()
    db.commit()

def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: str):
    db.query(models.Todo).filter(models.Todo.UUID == todo_id).delete()
    db.commit()

def get_todo_by_details_id(db: Session, details_id: str):
    return db.query(models.Todo).filter(models.Todo.DetailsUUID == details_id).all()



