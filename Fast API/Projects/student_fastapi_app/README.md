# Student CRUD API with JWT Authentication

A simple FastAPI project demonstrating CRUD operations with JWT-based authentication.

---

## 📘 Overview
This project implements:
- RESTful API design with FastAPI  
- CRUD operations on a student database  
- Pydantic models for data validation  
- JWT authentication using `OAuth2PasswordBearer`  
- Error handling with `HTTPException`  
- Testing via Swagger UI (`/docs`) 

---

## 🗂️ Project Structure
```
student_fastapi_app/
│
├── main.py
├── auth.py
├── models.py
└── utils.py
```
---

## ⚙️ Setup Instructions
1. **Install dependencies**
   ```bash
   pip install fastapi uvicorn python-jose bcrypt==4.0.1 passlib[bcrypt]==1.7.4
   ```
   
2. **Run the server**
```
uvicorn main:app --reload
```

3. Open API Docs

Go to: http://127.0.0.1:8000/docs

---

## 🔐 Authentication Flow

### 🪪 Login
- **Endpoint:** `/token`  
- **Username:** `admin`  
- **Password:** `admin123`  
- Copy the returned **`access_token`** from the response.

### ✅ Authorize
- Click **"Authorize"** in Swagger UI.  
- Paste your token as:  `Bearer <access_token>`



### 🧩 Access CRUD Endpoints
- After authorization, you can perform:  
- **Create** → `POST /students/{id}`  
- **Read** → `GET /students/{id}` or `GET /students/by-name/`  
- **Update** → `PUT /students/{id}`  
- **Delete** → `DELETE /students/{id}`
