from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.database import Base


class Jobs(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    company = Column(String)
    status = Column(String)
    location = Column(String)
    applied_on = Column(DateTime)
    source = Column(String)
    user_email = Column(String, ForeignKey('users.email'), index=True)  # Foreign key

    creator = relationship("Users", back_populates="jobs")


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)  # Foreign key - ForeignKey("Users.user_email")
    password = Column(String)

    jobs = relationship("Jobs", back_populates="creator")
