from sqlalchemy import Boolean, Column, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "Users"

    UUID = Column(String(36), primary_key=True, index=True, server_default="uuid()")
    Name = Column(String)
    PW = Column(String)
    Email = Column(String)

    CalendarDatabase = relationship("CalendarDatabase")
    Schedule = relationship("Schedule")


class CalendarDatabase(Base):
    __tablename__ = "CalendarDatabase"

    UUID = Column(String(36), primary_key=True, index=True, server_default="uuid()")
    DatabaseName = Column(String(1000))
    Members = Column(String(1000))
    Owner = Column(String(36), ForeignKey("Users.UUID"))

    Schedule = relationship("Schedule")


class Schedule(Base):
    __tablename__ = "Schedule"

    UUID = Column(String(36), primary_key=True, index=True, server_default="uuid()")
    ScheduleName = Column(String(1000))
    Owner = Column(String(36), ForeignKey("Users.UUID"))
    Editor = Column(String(1000))
    CalendarDatabase = Column(String, ForeignKey("CalendarDatabase.UUID"))
    Starts = Column(DateTime)
    Ends = Column(DateTime)
    AllDay = Column(Boolean)

    Detail = relationship("Detail")


class Detail(Base):
    __tablename__ = "Detail"

    UUID = Column(String(36), primary_key=True, index=True, server_default="uuid()")
    ScheduleUUID = Column(String(36), ForeignKey("Schedule.UUID"))
    Memo = Column(String(1000))
    CreatedAt = Column(DateTime)
    UpdatedAt = Column(DateTime)


class Todo(Base):
    __tablename__ = "Todo"

    UUID = Column(String(36), primary_key=True, index=True, server_default="uuid()")
    Schedule = Column(String(36), ForeignKey("Schedule.UUID"))
    TodoCheck = Column(Boolean)
    TodoContext = Column(String)

