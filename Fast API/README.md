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
