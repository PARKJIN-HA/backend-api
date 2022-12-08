import datetime
import uuid

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str = None


class TodoBase(BaseModel):
    UUID: str
    Details: int


class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    Details: int
    TodoCheck: bool = None
    TodoList: str = None

    class Config:
        orm_mode = True


class DetailsBase(BaseModel):
    UUID: str
    ScheduleUUID: str
    CreatedAt: datetime.datetime
    UpdatedAt: datetime.datetime


class DetailsCreate(DetailsBase):
    pass


class Details(DetailsBase):
    Memo: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    Name: str
    Email: str
    UUID: str = uuid.uuid4()


class UserCreate(UserBase):
    PW: str


class User(UserBase):
    class Config:
        orm_mode = True


# CREATE TABLE IF NOT EXISTS CalendarDatabase(
#     UUID VARCHAR(36) NOT NULL DEFAULT (uuid()) PRIMARY KEY,
# DatabaseName VARCHAR(1000) NOT NULL,
# Members VARCHAR(1000),
# Owner VARCHAR(36) NOT NULL,
# Foreign Key (Owner) REFERENCES Users (UUID) ON DELETE CASCADE
# );


class CalendarDatabaseBase(BaseModel):
    UUID: str = None
    DatabaseName: str = None
    Members: str = None
    Owner: str = None


class CalendarDatabaseCreate(CalendarDatabaseBase):
    UUID: str = None
    DatabaseName: str = None
    Owner: str = None


class CalendarDatabaseDelete(CalendarDatabaseBase):
    pass


class CalendarDatabase(CalendarDatabaseBase):
    class Config:
        orm_mode = True


class ScheduleBase(BaseModel):
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

    class Config:
        orm_mode = True
