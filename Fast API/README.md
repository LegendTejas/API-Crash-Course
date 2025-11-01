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

---

## 🚀 Fast API Full Course (Follow Step by Step Process to master it)


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

```

to run the server we will type this in terminal:
```
blog.main:app --reload
```








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
