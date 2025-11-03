# FastAPI-Course ⚡

This repository contains multiple **FastAPI projects and examples** to learn and master API development using FastAPI.  
It covers everything from basics to advanced features with hands-on implementations.

---

## 📌 Contents
- **Basics**
  - Hello World in FastAPI  
  - Path & Query Parameters  
  - Request Body and Data Validation (Pydantic)  
- **CRUD Operations**
  - Create, Read, Update, Delete APIs  
  - Database Integration (SQLite/MySQL)  
- **Authentication & Authorization**
  - JWT Authentication  
  - OAuth2  
- **Middleware & Dependencies**
  - Custom Middleware  
  - Dependency Injection  
- **Advanced Features**
  - Async Programming  
  - Background Tasks  
  - File Uploads & Downloads  
- **Deployment**
  - Running with Uvicorn  
  - Deployment on Cloud  

---

## 🛠️ Tech Stack
- Python 3.x  
- FastAPI  
- Uvicorn (ASGI server)  
- Pydantic  
- SQLAlchemy / Databases  
- Postman / cURL (for testing)  

---


# 🚀 Fast API Full Course (Follow Step by Step Process to master it)

---
# PART 1


### 1. Create a virtual environment and pip install fastapi

```
python -m venv fastapi-env
```

- We need to activate the virtual environment now:

```
source venv/bin/activate # Mac/Linux
fastapi-env\Scripts\activate # Windows
```

- Install fastapi

```
pip install fastapi
```

### 2. You also need an ASGI server, for production such as Uvicorn or Hypercorn:

```
pip install uvicorn
```

### 3. Create a main.py file

```
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': {'name':'Tejas'}}

@app.get('/about')
def about():
    return {'data': 'about page'}
```

### 4. Run the server with 

```
(fastapi-env) PS E:\FastAPI> uvicorn main:app --reload


INFO:     Will watch for changes in these directories: ['E:\\FastAPI']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [20136] using StatReload
INFO:     Started server process [15052]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Now click on the link http://127.0.0.1:8000 to see the output in server

<img width="300" height="200" alt="image" src="https://github.com/user-attachments/assets/dbff3967-9141-4458-8f23-d6d58fef7880" />


### 5. Path Parameters

we can add any parameter have a look:

```
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': 'blog list'}

@app.get('/blog/{id}')
def show(id : int):
    #fetch blog with id = id
    return {'data': id}
```

Now if we again reload the server 
``` 
uvicorn main:app --reload
```

It will show this on the server http://127.0.0.1:8000/blog/1

```
{
  "data": 1
}
```
Now you can change the id to 2, 3 or 100, etc.


- Ok now let's create another path for unpublished blogs
```
@app.get('blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}
```

again reload the server: http://127.0.0.1:8000/blog/unpublished
and in this way you can create multiple paths


### 6. API Docs - Swagger/ redocs

FastAPI provides an automatic documentation with Swagger UI where you can call and test your API directly from the browser http://127.0.0.1:8000/docs

<img width="1500" height="600" alt="image" src="https://github.com/user-attachments/assets/877c58a0-073f-4c36-94cd-4906a2ea9a01" />

Here we can try out all the methods GET, POST, PUT, DELETE and also see HTTPExceptions if any

- Similarly for redoc we will simply type: http://127.0.0.1:8000/redoc


### 7. Query Parameters

query parameters are used to send optional data in the URL (after ?) — for filtering, searching, sorting, or providing extra info without changing the route path.

```
@app.get('/')
def index(limit: int = 10, published: bool = True):
    # 'limit' and 'published' are query parameters
    if published:
        return {'data': f'{limit} published blogs from database'}
    else:
        return {'data': f'{limit} unpublished blogs'}
```

They are Accessed like:

- http://127.0.0.1:8000/?limit=5&published=true
- http://127.0.0.1:8000/?limit=3&published=false

**Why needed:**

They allow clients to customize requests (like pagination, filtering, search, etc.) without creating new endpoints.


### 8. Request Body

Let's see how POST method works:

```
from fastapi import FastAPI

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

@app.post('/blog')
def create_blog():
    return {'data': "Blog is created"}
```

Go to docs:
<img width="1200" height="700" alt="image" src="https://github.com/user-attachments/assets/409e4c91-96da-4279-ad86-aeaa9c073efc" />

Now to declare a **request body**, you use **Pydantic** models with all their power and benefits

- We have to import `BaseModel` from `pydantic`:

```
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
def create_blog(request: Blog):
    # Automatically validates input using Pydantic
    return request
```

Now in the FastAPI documentation there will be a new field "Request Body(required)"

<img width="884" height="498" alt="image" src="https://github.com/user-attachments/assets/fe37e8f0-820f-47ef-a4d1-c24bec2a9c9a" />

now let's try out:

```
@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f"Blog is creeated with title as {blog.title}"}
```

<img width="600" height="250" alt="image" src="https://github.com/user-attachments/assets/f7c1ff58-6ef1-42b3-834e-7c99bc56c14a" />

<img width="600" height="230" alt="image" src="https://github.com/user-attachments/assets/d1af4bf9-a870-49ca-a6ce-26201ca33e13" />


### 9. Debugging FastAPI Application

#### Ways to Debug a FastAPI Application

#### 1. Enable Debug Mode
- When creating your app, FastAPI’s `debug=True` helps show detailed error messages:
```python
app = FastAPI(debug=True)
```
➡️ Shows full traceback and error details in the browser — useful for development.

#### 2. Run Uvicorn with --reload
Automatically reloads the server when you make code changes:
```
uvicorn main:app --reload
```
➡️ Saves time and ensures you always test the latest code.

#### 3. Use print() or logging
Add temporary print or logging statements to inspect variable values or flow:
```
import logging
logging.basicConfig(level=logging.INFO)

@app.get("/debug")
def test_debug():
    x = 10
    logging.info(f"x value: {x}")
    return {"x": x}
```

#### 4. Use Debugging Tools in VS Code or PyCharm

- Set breakpoints
- Run in debug mode
- Step through code line by line


### 10. Pydantic Schemas and Database Connection

Let's create a new folder "blog" and inside that we will create all these .py files

Folder Structure:

```
  blog
    |- __init__.py
    |- main.py
    |- database.py
    |- schemas.py
```

main.py:
```
from fastapi import FastAPI # type: ignore
from . import schemas

app = FastAPI()


@app.post('/blog')
def create(request: schemas.Blog):
    return request
```

schemas.py:
```
from pydantic import BaseModel

class Blog(BaseModel):
    title:str
    body:str
```

to run the server we will type this in terminal:
```
uvicorn blog.main:app --reload
```

Now we will establish the database connection to store all the information from `Request body`
to the database so for that we will be using `SQLAlchemy`. Now to import it we need to install it: 
```
pip install sqlalchemy
```

- so let's create a db first `blog.db`

- Now in database.py:
```
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:/// ./blog.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args ={
    "check_same_thread": False
})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
```

- **Creating Model & Tables**

Let's create table

models.py:
```
from sqlalchemy import Column, Integer, String
from database import Base

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
```

To run it we need this line: `models.Base.metadata.create_all(engine)`

So we will make modifications in main.py:
```
from fastapi import FastAPI # type: ignore
from . import schemas, models
from .database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)

@app.post('/blog')
def create(request: schemas.Blog):
    return request
```

And now if we reload server we will have table in the database `blog.db` you can view it in VS Code with `SQLite Viewer` Extension:

<img width="737" height="345" alt="image" src="https://github.com/user-attachments/assets/09662a0b-c5c9-4632-9aba-17a328a06660" />


### 11. Store Blog to Database

main.py:
```
from fastapi import FastAPI, Depends # type: ignore
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog')
def create(request: schemas.Blog, db : Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
```

Now on reloading server in POST we can add data in the db:
```
{
  "title": "Tejas Blog",
  "body": "My Blog Body"
}
```

Now let's add one more row:
```
{
  "title": "second blog",
  "body": "blog body 2"
}
```

<img width="602" height="278" alt="image" src="https://github.com/user-attachments/assets/aee9de7f-9044-484d-a75a-4995ad0707a7" />


### 12. Store Blog to Database

Now let's create the GET method also inside main.py:
```
@app.get('/blog')
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs
```

And now if we reload server and execute GET we will have:

<img width="485" height="324" alt="image" src="https://github.com/user-attachments/assets/0b8f3c7e-9bfe-4f98-999a-05f3299560ae" />


Let's GET the data using ID for that add this code snippet in main.py:
```
@app.get('/blog/{id}')
def show(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog
```

on executing with ID = 2 we get the second row with ID = 2 i.e:

<img width="883" height="851" alt="image" src="https://github.com/user-attachments/assets/83e07268-1a19-4021-981f-fd009c9a0315" />

But what about any ID other than 1 and 2 (like 3) on executing id = 3 we will get response as `null` but there is a better way to get the response and handle errors so here comes Error handling with HTTPException and Status Code


### 13. HTTPException & Status Code

We can manually give the status code like this:
```
@app.post('/blog', status_code=201)
```

HTTP status code 201 means **Created** — The request succeeded, and a new resource was created on the server.

- Now what if we dont know the exact status code to use where then in that case we can use the `fatapi.status` to get the status code recommendations

Example:
```
from fastapi import FastAPI, status

app = FastAPI()

@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create_blog(name: str):
    return {"name": name}
```

Now let's improve the code and response for our previous problem in id other than 1 and 2 
<img width="373" height="231" alt="image" src="https://github.com/user-attachments/assets/e4fee9dc-4c64-48eb-8660-786e7a810be6" />

so to handle the status code and null response we will first have to import `HTTPException` from fastapi:

**main.py:**
```
from fastapi import FastAPI, Depends, status, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog')
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get('/blog/{id}', status_code=200)
def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )
    return blog
```

And now we got the proper Status Code and Response for this
<img width="696" height="285" alt="image" src="https://github.com/user-attachments/assets/445c4b91-8111-4d8d-b65d-1a1991247372" />


### 14. Delete a Blog

Example:

```
@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    # Query the blog by ID
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    # If blog doesn't exist, raise a 404 error
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )

    # Delete the blog if found
    blog.delete(synchronize_session=False)
    db.commit()
    return {"message": "Blog deleted successfully"}
```

Now reload the server and try out `DELETE` method and try deleting id = 2 it will get deleted.


### 15. Update a Blog

Example:

```
@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )

    blog.update(request.dict())
    db.commit()
    return {"message": "Updated successfully"}
```

Now reload and try out `UPDATE` method by updating title and body of id = 2
<img width="517" height="579" alt="image" src="https://github.com/user-attachments/assets/a37a5118-5ba9-4550-ae76-83c7920fbe2e" />



Let's execute the `GET` method to see changes:
<img width="482" height="337" alt="image" src="https://github.com/user-attachments/assets/1916e5b4-fb38-45f1-82e2-a02c25e7669e" />


so let's see the db it's updated:
<img width="605" height="267" alt="image" src="https://github.com/user-attachments/assets/d3ab873f-dbe2-4240-948c-6d457a0304a8" />

So till now we have seen all the 4 methods (GET, POST, PUT, DELETE)
<img width="912" height="600" alt="image" src="https://github.com/user-attachments/assets/caae3e9b-5fbb-4a08-a2a9-08d0287ad889" />

---

# PART 2

### 16. Response Model

Let's say we want to get blog by id 1 but we only want to get title only (no body and no id) then in that case we will use reponse body 

**Before:**
<img width="405" height="221" alt="image" src="https://github.com/user-attachments/assets/09b470f7-dbe9-4ace-8996-18f0b27b8a60" />

**After:**
<img width="260" height="141" alt="image" src="https://github.com/user-attachments/assets/d459966c-8fbf-423c-80f9-4c16de5bfb0f" />

**What Happens on using response body**

- Only the specified fields (here title) appear in the JSON response.
- AutoDocs (Swagger UI) also show this model.

A response model in FastAPI defines the structure and data type of the response that your API should return.
It helps ensure data validation, automatic documentation, and clean output (filters out extra/unwanted fields).

NOTE: we call a pydantic models as schemas so here the response model is response schema and sqlalchemy model as model (so don't get confused in model and schema)

- We use this in main.py: `@app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)`

to get title only our schemas.py will be:
```
from pydantic import BaseModel

class Blog(BaseModel):
    title:str
    body:str

class ShowBlog(BaseModel):
    title : str
    class Config():
        orm_mode = True
```

### 17. Create User

Here’s a simple example of how to create a user in FastAPI using a Pydantic model and a POST request

```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Pydantic model for request body
class User(BaseModel):
    username: str
    email: str
    age: int

# In-memory list to store users
users = []

@app.post("/users/")
def create_user(user: User):
    users.append(user)
    return {"message": "User created successfully!", "user": user}
```

**How it works**

- POST /users/ endpoint accepts a JSON body matching the User model.
- The data is automatically validated by FastAPI.
- The user is stored in a Python list (users).
- A success message with the user data is returned.

**Example Request (JSON)**
```
{
  "username": "tejas",
  "email": "tejas@example.com",
  "age": 21
}
```

**Example Response**
```
{
  "message": "User created successfully!",
  "user": {
    "username": "tejas",
    "email": "tejas@example.com",
    "age": 21
  }
}
```

Now let's create user for our blogs

Before that we have to `pip install "email-validator"` because Pydantic’s EmailStr type depends on an external package called `email-validator`

then make certain changes in these three files `main.py`, `models.py`, `schemas.py` :

### **schemas.py**
```
from pydantic import BaseModel, EmailStr

# ---------- Blog schemas ----------
class BlogBase(BaseModel):
    title: str
    body: str

class BlogCreate(BlogBase):
    pass

class ShowBlog(BlogBase):
    id: int

    class Config:
        from_attributes = True


# ---------- User schemas ----------
class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class ShowUser(UserBase):
    id: int

    class Config:
        from_attributes = True
```

### **models.py**
```
from sqlalchemy import Column, Integer, String
from .database import Base

# ORM model for 'blogs' table
class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)

class User(Base):
    __tablename__= 'users'

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
```

### **main.py**
```
from fastapi import FastAPI, Depends, status, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

# Create database tables (if they don't already exist)
models.Base.metadata.create_all(engine)


# Dependency to get a database session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------- BLOG ENDPOINTS ----------

# Create a blog (POST)
@app.post('/blog', response_model=schemas.ShowBlog, status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.BlogCreate, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# Delete a blog by ID (DELETE) - return JSON message with 200 OK
@app.delete('/blog/{id}', status_code=status.HTTP_200_OK)
def destroy(id: int, db: Session = Depends(get_db)):
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog_query.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )

    blog_query.delete(synchronize_session=False)
    db.commit()
    return {"message": "Blog deleted successfully"}


# Update a blog by ID (PUT)
@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.BlogCreate, db: Session = Depends(get_db)):
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog_query.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )

    blog_query.update(request.dict())
    db.commit()
    return {"message": "Updated successfully"}


# Get all blogs (GET)
@app.get('/blog', response_model=list[schemas.ShowBlog])
def all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


# Get a single blog by ID (GET)
@app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )
    return blog


# ---------- USER ENDPOINTS ----------

# Create user (POST)
@app.post('/user', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
    # optional: simple duplicate email check
    existing = db.query(models.User).filter(models.User.email == request.email).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with this email already exists"
        )

    new_user = models.User(
        name=request.name,
        email=request.email,
        password=request.password  # in production: hash the password before storing
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
```

To create new user first delete blog.db then restart your server:
```
del blog.db
```

then 
```
uvicorn blog.main:app --reload
```

Now try creating user:
<img width="875" height="793" alt="image" src="https://github.com/user-attachments/assets/b035eaee-e7ef-4657-9189-1edebd907715" />


And to confirm let's check the blog.db:
<img width="849" height="226" alt="image" src="https://github.com/user-attachments/assets/4bfd4f9f-e2d3-4f65-b46c-43f468150a77" />

So new user created successfully!!!

But the problem here is the password is not encrypted and can be misused so now let's look at hashing/encrypting passwords

### 18. Hash Password

Now we need passlib library to handle password hashes
```
pip install passlib
pip install "bcrypt<4.0"
```
This installs bcrypt 3.2.2, which works perfectly with Passlib.

Let's create a new file `hashing.py` :

```
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes = ["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        hashedPassword = pwd_cxt.hash(password)
        return hashedPassword
```

then we will simply import this file in `main.py` and use it to hash password:
```
from fastapi import FastAPI, Depends, status, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from .hashing import Hash #importing Hash class from hashing.py file

app = FastAPI()

# Create database tables (if they don't already exist)
models.Base.metadata.create_all(engine)


# Dependency to get a database session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create a blog (POST)
@app.post('/blog', response_model=schemas.ShowBlog, status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.BlogCreate, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# Delete a blog by ID (DELETE) - return JSON message with 200 OK
@app.delete('/blog/{id}', status_code=status.HTTP_200_OK)
def destroy(id: int, db: Session = Depends(get_db)):
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog_query.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )

    blog_query.delete(synchronize_session=False)
    db.commit()
    return {"message": "Blog deleted successfully"}


# Update a blog by ID (PUT)
@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.BlogCreate, db: Session = Depends(get_db)):
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog_query.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )

    blog_query.update(request.dict())
    db.commit()
    return {"message": "Updated successfully"}


# Get all blogs (GET)
@app.get('/blog', response_model=list[schemas.ShowBlog])
def all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


# Get a single blog by ID (GET)
@app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )
    return blog


# Create user (POST)
@app.post('/user', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
    # optional: simple duplicate email check
    existing = db.query(models.User).filter(models.User.email == request.email).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with this email already exists"
        )
    new_user = models.User(
        name=request.name,
        email=request.email,
        password= Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
```


Now try executing this:
<img width="269" height="133" alt="image" src="https://github.com/user-attachments/assets/211a76eb-6738-4b10-a253-a5e4b0b311d8" />

Now if we check the blog.db , The password is hashed
<img width="921" height="131" alt="image" src="https://github.com/user-attachments/assets/58d7d325-ed85-412f-938f-52bf5597e1f6" />


Let's create 4 more users:
<img width="976" height="251" alt="image" src="https://github.com/user-attachments/assets/140bc37d-03e5-4dbc-90ae-f19c2d5e4d25" />

Now we have 5 users let show user with username and email only(no password and id) so for that again we use pydantic schemas

make these changes in `schemas.py`:
```
# ---------- User schemas ----------
class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    class Config:
        from_attributes = True
```

Let's get user by their IDs

add these in `main.py`:
```
@app.get('/user/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User with this id {id} is not available")
    
    return user
```

On executing we can get any user with id
<img width="1592" height="847" alt="image" src="https://github.com/user-attachments/assets/51adf473-2e16-443f-b95c-725c66d6446d" />


### 19. Using Docs Tags

Use the `tags` parameter with your path operations (and `APIRounter`s) to assign them to different tags:

Example:
```
@app.get("/users/", tags=["users"])
```

```
@app.get("/blogs/", tags=["blogs"])
```

<img width="912" height="705" alt="image" src="https://github.com/user-attachments/assets/3e6decf5-db84-411e-8236-d5498deaed57" />


### 20. Relationships

To create relationships we use `relationship` provided by SQLAlchemy ORM

This will become, more or less, a "magic" attribute that will contain the values from other tables related to this one.

Let's add a foreign key "user_id" (from "id" column in "user" table) to the "blogs" table

NOTE: first delete blog.db then refresh the server and make changes in the `models.py` and `schemas.py`:

### **models.py**:
```
from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

# ORM model for 'blogs' table
class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="blogs")


class User(Base):
    __tablename__= 'users'

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship('Blog', back_populates = "creator")
```

### **schemas.py**:
```
from pydantic import BaseModel, EmailStr


# ---------- Blog Schemas ----------

class BlogBase(BaseModel):
    title: str
    body: str


# Request schema for creating a blog
class BlogCreate(BlogBase):
    user_id: int  # Added user_id for linking blog with user

    class Config:
        from_attributes = True


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

    class Config:
        from_attributes = True


# Response schema for showing blog details (with creator info)
class ShowBlog(BaseModel):
    id: int
    title: str
    body: str
    creator: ShowUser   # establishes relationship

    class Config:
        from_attributes = True
```

also modify the `main.py` with these changes:
```
@app.post('/blog', response_model=schemas.ShowBlog, status_code=status.HTTP_201_CREATED, tags=['blogs'])
def create_blog(request: schemas.BlogCreate, db: Session = Depends(get_db)):
    # Automatically assign user_id (e.g., 1)
    default_user_id = 1

    # Check if user exists
    user = db.query(models.User).filter(models.User.id == default_user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {default_user_id} not found. Please create a user first."
        )

    new_blog = models.Blog(
        title=request.title,
        body=request.body,
        user_id=default_user_id
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
```

<img width="947" height="201" alt="image" src="https://github.com/user-attachments/assets/794fe35a-4a2a-4b2f-9a06-0404d122477d" />

Let's create user to see changes
<img width="391" height="458" alt="image" src="https://github.com/user-attachments/assets/8209e01e-f162-4a90-bcd6-02b04531247c" />

<img width="994" height="193" alt="image" src="https://github.com/user-attachments/assets/032a2daa-45bc-4024-b7cb-97af3ef5f1e3" />

Now let's create new blog:
<img width="477" height="515" alt="image" src="https://github.com/user-attachments/assets/6136a154-dc48-4801-bbf9-5f8386c4563b" />

<img width="445" height="250" alt="image" src="https://github.com/user-attachments/assets/6ac50d60-9bab-42c9-b957-ebfa29182cc1" />

Now let's check the "blogs" table in blog.db:
<img width="883" height="197" alt="image" src="https://github.com/user-attachments/assets/5971f931-0292-4319-b03e-22d264eb831f" />



Now let's assign all the blogs creator to one user "Tejas" for that we need to modify `schemas.py`:

```
from pydantic import BaseModel, EmailStr
from typing import List

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


# Response schema for showing blog details (with creator info)
class ShowBlog(BaseModel):
    id: int
    title: str
    body: str
    creator: ShowUser   # establishes relationship

    class Config:
        from_attributes = True
```

Now let's create one more blog:
<img width="334" height="188" alt="image" src="https://github.com/user-attachments/assets/a5699f43-4bb0-4b74-8872-a366b82fa701" />

and execute it we will get:
<img width="444" height="415" alt="image" src="https://github.com/user-attachments/assets/c391b1bf-ef92-4be3-bc71-088a17cc9670" />


---

# PART 3

### 21. API Router













---

## 🎯 Goals
- Learn **FastAPI** through real-world projects  
- Build **scalable, secure, and efficient APIs**  
- Understand best practices of API development and deployment  

---

## 📖 Resources
- [FastAPI Documentation](https://fastapi.tiangolo.com/)  
- [Pydantic Documentation](https://docs.pydantic.dev/)  
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

---

## 🤝 Contributing
Contributions are welcome!  
Feel free to fork this repo and submit pull requests with improvements.  

---

## 📜 License
This project is licensed under the MIT License.  
