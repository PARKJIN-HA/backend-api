from sqlalchemy import Boolean, Column, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "Users"

    UUID = Column(String(36), primary_key=True, index=True, server_default="uuid()")
    Name = Column(String)
    PW = Column(String)
    Email = Column(String)

    schedule = relationship("Schedule", back_populates="user")
    database = relationship("CalendarDatabase", back_populates="user")


class CalendarDatabase(Base):
    __tablename__ = "CalendarDatabase"

    UUID = Column(String(36), primary_key=True, index=True, server_default="uuid()")
    DatabaseName = Column(String(1000))
    Members = Column(String(1000))
    Owner = Column(String(36), ForeignKey("Users.UUID"))

    user = relationship("User", back_populates="database")
    schedule = relationship("Schedule", back_populates="database")


class Schedule(Base):
    __tablename__ = "Schedule"

    UUID = Column(String(36), primary_key=True, index=True, server_default="uuid()")
    ScheduleName = Column(String(1000))
    Owner = Column(String(36), ForeignKey("Users.UUID"))
    Editor = Column(String(1000))
    CalendarDatabase = Column(String, ForeignKey("CalendarDatabase.UUID"))
    Starts = Column(DateTime)
    Ends = Column(DateTime)

    user = relationship("User", back_populates="schedule", uselist=False)
    database = relationship("CalendarDatabase", back_populates="schedule", uselist=False)
    detail = relationship("Detail", back_populates="schedule", uselist=False)
    todo = relationship("Todo", back_populates="schedule", uselist=False)


class Detail(Base):
    __tablename__ = "Detail"

    UUID = Column(String(36), primary_key=True, index=True, server_default="uuid()")
    ScheduleUUID = Column(String(36), ForeignKey("Schedule.UUID"))
    Memo = Column(String(1000))
    CreatedAt = Column(DateTime)
    UpdatedAt = Column(DateTime)

    schedule = relationship("Schedule", back_populates="detail", uselist=False)


class Todo(Base):
    __tablename__ = "Todo"

    UUID = Column(String(36), primary_key=True, index=True, server_default="uuid()")
    Schedule = Column(String(36), ForeignKey("Schedule.UUID"))
    TodoCheck = Column(Boolean)
    TodoContext = Column(String)

    schedule = relationship("Schedule", back_populates="todo", uselist=False)
