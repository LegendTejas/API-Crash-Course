from pydantic import BaseModel, EmailStr
from typing import List, Optional

# ---------- Blog Schemas ----------

class BlogBase(BaseModel):
    title: str
    body: str
    class Config:
        from_attributes = True

# Request schema for creating a blog
class BlogCreate(BlogBase):
    user_id: int  # Added user_id for linking blog with user

    class Config:
        from_attributes = True

class BlogUpdate(BlogBase):
    pass


# ---------- User Schemas ----------

class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


# Response schema for showing user details (without password)
class ShowUser(BaseModel):
    id: int
    name: str
    email: str
    blogs: List[BlogBase] = []
    class Config:
        from_attributes = True


# Response schema for showing blog details (without creator info)
class ShowBlog(BaseModel):
    id: int
    title: str
    body: str
    class Config:
        from_attributes = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None