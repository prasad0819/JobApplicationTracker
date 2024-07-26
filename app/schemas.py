from datetime import date
from pydantic import BaseModel, ConfigDict
from typing import Optional, List


class User(BaseModel):
    # password: str
    id: int
    first_name: str
    last_name: str
    email: str

    class ConfigDict:
        from_attributes = True


class Job(BaseModel):
    id: int
    title: str
    company: str
    status: str
    location: Optional[str] = None
    applied_on: date
    source: str

    class ConfigDict:
        from_attributes = True
    # user_email : str [Foreign key?]


class CreateUser(User):
    password: str

    class ConfigDict:
        from_attributes = True


class CreateJob(Job):
    pass

    class ConfigDict:
        from_attributes = True


class ShowUser(BaseModel):
    # password: str
    id: int
    first_name: str
    last_name: str
    email: str
    # jobs: List[Job] = []

    class ConfigDict:
        from_attributes = True


class ShowJob(BaseModel):
    id: int
    title: str
    company: str
    status: str
    location: Optional[str] = None
    applied_on: date
    source: str
    creator: ShowUser

    class ConfigDict:
        from_attributes = True
    # user_email : str [Foreign key?]


class Login(BaseModel):
    email: str
    password: str

    class ConfigDict:
        from_attributes = True
