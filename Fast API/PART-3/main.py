from fastapi import FastAPI
from typing import Optional  # Used to mark fields as optional (can be None)
from pydantic import BaseModel  # Base class for creating data models in FastAPI (for validation and serialization)


app = FastAPI()

@app.get('/')
def index(limit: int = 10, published: bool = True):
    # 'limit' and 'published' are query parameters
    if published:
        return {'data': f'{limit} published blogs from database'}
    else:
        return {'data': f'{limit} unpublished blogs'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'1', '2'}}

# Data Model for POST Request
class Blog(BaseModel):
    title: str             # Blog title
    body: str              # Blog content
    published: Optional[bool]  # Optional field, defaults to None if not provided

# POST Route with Request Body
@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f"Blog is creeated with title as {blog.title}"}