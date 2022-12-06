from sqlalchemy.orm import Session

import models
import schemas


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
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


def create_database(db: Session, database: schemas.CalendarDatabaseCreate):
    db_database = models.CalendarDatabase(**database.dict())
    db.add(db_database)
    db.commit()
    db.refresh(db_database)
    return db_database


def delete_database(db: Session, database_id: str):
    db.query(models.CalendarDatabase).filter(models.CalendarDatabase.UUID == database_id).delete()
    db.commit()


def get_databases(db: Session, owner_id: str):
    return db.query(models.CalendarDatabase).filter(models.CalendarDatabase.Owner == owner_id).all()


def create_schedule(db: Session, schedule: schemas.ScheduleCreate):
    db_schedule = models.Schedule(**schedule.dict())
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule


def delete_schedule(db: Session, schedule_id: str):
    db.query(models.Schedule).filter(models.Schedule.UUID == schedule_id).delete()
    db.commit()


def get_schedules(db: Session, user_id: str):
    return db.query(models.Schedule).filter(models.Schedule.Owner == user_id).all()


# def get_schedules(db: Session, schedule_id: str):
#     return db.query(models.Schedule).filter(models.Schedule.UUID == schedule_id).first()


def create_details(db: Session, details: schemas.DetailsCreate):
    db_details = models.Detail(**details.dict())
    db.add(db_details)
    db.commit()
    db.refresh(db_details)
    return db_details


def delete_details(db: Session, details_id: str):
    db.query(models.Detail).filter(models.Detail.UUID == details_id).delete()
    db.commit()


def get_details(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Detail).offset(skip).limit(limit).all()


def get_details_by_schedule_id(db: Session, schedule_id: str):
    return db.query(models.Detail).filter(models.Detail.ScheduleUUID == schedule_id).all()


def create_schedule_details(db: Session, schedule_id: str, details_id: str):
    db_details = models.Detail(UUID=details_id, ScheduleUUID=schedule_id)
    db.add(db_details)
    db.commit()
    db.refresh(db_details)
    return db_details


def delete_details_by_schedule_id(db: Session, schedule_id: str):
    db.query(models.Detail).filter(models.Detail.ScheduleUUID == schedule_id).delete()
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
