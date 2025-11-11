from sqlalchemy import Column, Integer, String
from .database import Base

# ORM model for 'blogs' table
class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)