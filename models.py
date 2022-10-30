from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "Users"

    UUID = Column(String, primary_key=True, index=True, server_default="uuid()")
    Name = Column(String)
    PW = Column(String)
    Email = Column(String)

    Schedule = relationship("Schedule", back_populates="user")


class Schedule(Base):
    __tablename__ = "Schedule"

    UUID = Column(String, primary_key=True, index=True, server_default="uuid()")
    ScheduleName = Column(String, index=True)
    Owner = Column(Integer, ForeignKey("Users.UUID"))
    Members = Column(String)
    Category = Column(String)
    Starts = Column(DateTime)
    Ends = Column(DateTime)

    user = relationship("User", back_populates="Schedule", uselist=False)


class Details(Base):
    __tablename__ = "Details"

    UUID = Column(String, primary_key=True, index=True, server_default="uuid()")
    ScheduleUUID = Column(Integer, ForeignKey("Schedule.UUID"))
    Memo = Column(String)
    CreatedAt = Column(DateTime)
    UpdatedAt = Column(DateTime)

    todo = relationship("Todo", back_populates="details", uselist=False)


class Todo(Base):
    __tablename__ = "Todo"

    UUID = Column(String, primary_key=True, index=True, server_default="uuid()")
    Details = Column(Integer, ForeignKey("Details.UUID"))
    TodoCheck = Column(Boolean)
    TodoList = Column(String)

    details = relationship("Details", back_populates="todo", uselist=False)
