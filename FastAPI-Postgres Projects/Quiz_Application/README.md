# 📚 Quiz Application Project using FastAPI and PostgreSQL

A simple and scalable backend for managing quiz questions and choices.  
Built using **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.

---

## Features

- Create quiz questions with multiple choices  
- Mark correct/incorrect options  
- Retrieve questions and choices from the database  
- PostgreSQL database integration  
- Fully RESTful API  
- Clean and organized project structure  

---

## Tech Stack

- **FastAPI** (Backend framework)  
- **PostgreSQL** (Database)  
- **SQLAlchemy** (ORM)  
- **Pydantic** (Data validation)  
- **Uvicorn** (ASGI server)  

---

## ▶️ How to Run the Project

### **1. Clone the repository**
```bash
git clone <your-repo-url>
cd <your-project-folder>
```

### **2. Create and activate a virtual environment**
```
python -m venv venv
venv\Scripts\activate
```

### **3. Install dependencies**
```
pip install -r requirements.txt
```

### **4. Setup Postgres using pgAdmin4**


### **5. Configure your PostgreSQL database**

Create a database in PostgreSQL: (See Query1,2,3))
```
CREATE DATABASE quizappdb;
```

**Update your database connection inside database.py:**
```
URL_DATABASE = "postgresql://postgres:YOUR_PASSWORD@localhost:5432/quizappdb"
```

### **6. Run the FastAPI server**
```
uvicorn main:app --reload
```

API will be available at:
```
http://127.0.0.1:8000
```

## **API Endpoints**

### **Create a Question**
```
POST /questions/
```

**Example Request Body:**
```
{
  "question_text": "Which data structure uses FIFO?",
  "choices": [
    { "choice_text": "Stack", "is_correct": false },
    { "choice_text": "Queue", "is_correct": true }
  ]
}
```

### **Get a Question**
```
GET /questions/{question_id}
```

### **Get Choices of a Question**
```
GET /choices/{question_id}
```

**Testing the API**

You can test all API routes using FastAPI's built-in Swagger UI:
```
http://127.0.0.1:8000/docs
```

**View Tables inside quizappdb: `questions` and `choices`**
```
SELECT * FROM questions;
```
<img width="612" height="113" alt="image" src="https://github.com/user-attachments/assets/5c417f77-f824-465b-b7c3-3fc6057f52cc" />


```
SELECT * FROM choices;
```
<img width="540" height="298" alt="image" src="https://github.com/user-attachments/assets/240dfe20-d325-4fd7-9702-4c03d021c162" />
