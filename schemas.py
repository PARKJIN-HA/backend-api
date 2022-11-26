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


class ScheduleBase(BaseModel):
    UUID: str = uuid.uuid4()
    ScheduleName: str
    Owner: str
    Category: str
    Starts: datetime.datetime

class ScheduleCreate(ScheduleBase):
    pass

class ScheduleDelete(ScheduleBase):
    UUID: str

class Schedule(ScheduleBase):
    Ends: datetime.datetime = None
    Members : list[User] = None

    class Config:
        orm_mode = True

