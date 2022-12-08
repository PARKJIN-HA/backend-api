import datetime
import uuid

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str = None


class TodoBase(BaseModel):
    class Config:
        orm_mode = True

    UUID: str
    Details: int


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    Details: int
    TodoCheck: bool = None
    TodoList: str = None


class DetailsBase(BaseModel):
    class Config:
        orm_mode = True

    UUID: str
    ScheduleUUID: str
    CreatedAt: datetime.datetime
    UpdatedAt: datetime.datetime


class DetailsCreate(DetailsBase):
    pass


class Details(DetailsBase):
    Memo: str


class UserBase(BaseModel):
    class Config:
        orm_mode = True

    Name: str
    Email: str
    UUID: str = uuid.uuid4()


class UserCreate(UserBase):
    PW: str


class User(UserBase):
    pass


class CalendarDatabaseBase(BaseModel):
    UUID: str = None
    DatabaseName: str = None
    Members: str = None
    Owner: str = None

    class Config:
        orm_mode = True


class CalendarDatabaseCreate(CalendarDatabaseBase):
    UUID: str = None
    DatabaseName: str = None
    Owner: str = None


class CalendarDatabaseDelete(CalendarDatabaseBase):
    pass


class CalendarDatabase(CalendarDatabaseBase):
    pass


class ScheduleBase(BaseModel):
    class Config:
        orm_mode = True

    UUID: str = None
    ScheduleName: str = None
    Owner: str = None
    CalendarDatabase: str = None
    Starts: datetime.datetime = None


class ScheduleCreate(ScheduleBase):
    UUID: str
    ScheduleName: str
    Owner: str
    CalendarDatabase: str
    Starts: datetime.datetime


class ScheduleDelete(ScheduleBase):
    UUID: str


class Schedule(ScheduleBase):
    Ends: datetime.datetime = None
    Members: list[User] = None
