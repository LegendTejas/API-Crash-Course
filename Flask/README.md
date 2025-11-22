# Flask

## 1. INTRODUCTION TO FLASK

Flask is a lightweight and flexible web framework for Python. It is known as a micro-framework because it provides only the essential tools needed to build web applications, without enforcing a specific project structure or including unnecessary components. This makes Flask simple to learn, easy to use, and highly extensible.

Flask allows developers to create web servers, handle routes (URLs), process user requests, render HTML templates, connect with databases, and build APIs. It follows the WSGI (Web Server Gateway Interface) standard and uses Jinja2 as its templating engine.

Because of its simplicity and modular design, Flask is widely used for small to medium applications, APIs, and rapid prototyping. Developers can add extensions for authentication, database ORM, form handling, and more depending on the project requirements.


## 3. User Guide 
### (Step by Step Follow along to master Flask Web Development)

### **Step 1: Create a folder and open in VS Code then create virtual environment inside it:**
```
python -m venv flask-env  
```

- then activate it:
```
source venv/bin/activate # Mac/Linux
fastapi-env\Scripts\activate # Windows
```

- install flask
```
pip install flask
```
---

### **Step 2: Create a app.py file**
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/home')
def products():
    return "this is home page"

if __name__ == "__main__":
    app.run(debug=True, port=8000)
```

now run it in the same terminal
```
python app.py
```

the terminal will start the server
```
(flask-env) PS C:\Users\hp\OneDrive\Desktop\flask> python app.py
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:8000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 128-086-733
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
127.0.0.1 - - [22/Nov/2025 16:18:33] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [22/Nov/2025 16:18:33] "GET /favicon.ico HTTP/1.1" 404 -  
```

Now go to localhost 8000  `http://127.0.0.1:8000/ ` you will see

<img width="517" height="180" alt="image" src="https://github.com/user-attachments/assets/bcee9c19-21e1-4b67-9f00-85f9963afe85" />

and since we have created one more route for `home` in app.py so if you type this `http://127.0.0.1:8000/home ` you will see home page

<img width="520" height="165" alt="image" src="https://github.com/user-attachments/assets/018f3a9f-ea51-4c18-adc9-8e42c0cebe85" />

---

### **Step 3: static and templates directories**

#### **NOTE:**
In Flask, `static` and `templates` are two special folders used to organize files that your web application needs.

**1. `templates` Folder**

The `templates` folder stores all your HTML files that Flask will render using the Jinja2 templating engine.

**Purpose**

- To render HTML pages with dynamic data.
- To separate design (HTML) from backend logic (Python).
- To use template inheritance (e.g., `base.html` → `home.html`).

Examples of files inside `templates/`:
```
index.html

login.html

dashboard.html

base.html
```

Example:
```
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
```

**2. `static` Folder**

The `static` folder stores all files that do not change dynamically, such as:

**Common static files**

- CSS (e.g., style.css)
- JavaScript (e.g., script.js)
- Images (e.g., logo.png)
- Fonts
- Custom assets

**Purpose**

To serve static content such as styling, frontend scripts, and assets.

**Usage in HTML**

```
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<img src="{{ url_for('static', filename='logo.png') }}" alt="Logo">
```

So the folder structure will be like this:

```
project/
│
├── app.py
├── static/
│     ├── style.css
│     └── logo.png
└── templates/
      ├── index.html
      └── about.html
```

---

Now what you have to do is make 2 folders static and templates
