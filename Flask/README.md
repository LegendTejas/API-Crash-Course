# Flask

## 1. INTRODUCTION TO FLASK

Flask is a lightweight and flexible web framework for Python. It is known as a micro-framework because it provides only the essential tools needed to build web applications, without enforcing a specific project structure or including unnecessary components. This makes Flask simple to learn, easy to use, and highly extensible.

Flask allows developers to create web servers, handle routes (URLs), process user requests, render HTML templates, connect with databases, and build APIs. It follows the WSGI (Web Server Gateway Interface) standard and uses Jinja2 as its templating engine.

Because of its simplicity and modular design, Flask is widely used for small to medium applications, APIs, and rapid prototyping. Developers can add extensions for authentication, database ORM, form handling, and more depending on the project requirements.

---

## 2. USER GUIDE
### (Step by Step Follow along to master Flask Web Development)

First download all necessary modules from requirements.txt] 

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

and in `templates/` create `index.html` and paste this code of bootstrap for a Todo app:
```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My Todo</title>

    <!-- Bootstrap CSS -->
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
      rel="stylesheet"
    />
  </head>
  <body>
    <nav class="navbar navbar-expand-lg bg-primary" data-bs-theme="dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">My Todo App</a>

        <!-- Toggler -->
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-label="Toggle navigation"
          title="Toggle navigation"
        >
          <span class="navbar-toggler-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Toggle navigation</span>
        </button>

        <!-- Menu -->
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#"
                >Home</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Features</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Pricing</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Contact</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <div class="container my-3">
        <h2>Add a To-Do</h2>
        <form>
  <div class="mb-3">
    <label for="todotitle" class="form-label">Todo Title</label>
    <input type="text" class="form-control" id="todotitle" aria-describedby="title">
  </div>
  <div class="mb-3">
    <label for="desc" class="form-label">Todo Description</label>
    <input type="text" class="form-control" id="desc">
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
    </div>

    <div class="container my-4">
        <h2>Your To-Do List</h2>
        <table class="table">
  <thead>
    <tr>
      <th scope="col">S.No</th>
      <th scope="col">First</th>
      <th scope="col">Last</th>
      <th scope="col">Handle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>Jacob</td>
      <td>Thornton</td>
      <td>@fat</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>John</td>
      <td>Doe</td>
      <td>@social</td>
    </tr>
  </tbody>
</table>
    </div>
    <!-- Bootstrap JS -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
    ></script>
  </body>
</html>
```

---

### **Step 4: Creating Database for Todo app**

update `app.py`:

```
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"   # fixed typo

# ---- CREATE DATABASE AUTOMATICALLY ----
with app.app_context():
    db.create_all()
# ---------------------------------------


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/home')
def products():
    return "this is home page"


if __name__ == "__main__":
    app.run(debug=True, port=8000)
```

This code creates a Flask web app and connects it to a SQLite database named todo.db using Flask-SQLAlchemy. A Todo model (table) is defined with columns for ID, title, description, and creation date. Then, inside the application context, db.create_all() automatically creates the database and the table before the server starts. Two routes are defined: / renders an HTML template, and /home returns simple text. Finally, the Flask app runs in debug mode on port 8000.


Now our todo.db is created inside instance folder check it using sqlite viewer

So to add data in the db we have to modify @app.route('/') inside `app.py`:
```
@app.route('/')
def hello_world():
    todo = Todo(title="First Todo", desc="Start investing in Stock Market")
    db.session.add(todo)
    db.session.commit()
    return render_template('index.html')
```

then go to our site `http://127.0.0.1:8000/` and refresh it 4 times or how much data you want so now when you open `todo.db` you will see the data

<img width="1188" height="345" alt="image" src="https://github.com/user-attachments/assets/a7b7f617-e254-4166-ac6d-d8521e292fce" />

---

### **Step 5: Querying records**

- First download extension `Jinja2 Snippet Kit` to use Jinja Templating

- Now update `app.py`:
make changes in `@app.route('/home')`:

```
@app.route('/home')
def products():
    allTodo = Todo.query.all()
    print(allTodo)
    return "this is home page"
```

Now run `python app.py` and go to `http://127.0.0.1:8000/home` and now you will see all the data in the terminal:
```
[1 - First Todo, 2 - First Todo, 3 - First Todo, 4 - First Todo]
127.0.0.1 - - [23/Nov/2025 11:39:22] "GET /home HTTP/1.1" 200 -
```

- make changes in `@app.route('/')` to show the data in our website:
```
@app.route('/')
def hello_world():
    todo = Todo(title="First Todo", desc="Start investing in Stock Market")
    db.session.add(todo)
    db.session.commit()
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)
```

- now we will use jinja templating in `index.html` and make changes in `<tbody>`:
```
  <tbody>
    {% for todo in allTodo %}
    <tr>
      <th scope="row">{{loop.index}}</th>
      <td>{{todo.title}}</td>
      <td>{{todo.desc}}</td>
      <td>{{todo.date_created}}</td>
    </tr>
    {% endfor %}
```

so after making these changes our `index.html` will be like this:
```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My Todo</title>

    <!-- Bootstrap CSS -->
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
      rel="stylesheet"
    />
  </head>
  <body>
    <nav class="navbar navbar-expand-lg bg-primary" data-bs-theme="dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">My Todo App</a>

        <!-- Toggler -->
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-label="Toggle navigation"
          title="Toggle navigation"
        >
          <span class="navbar-toggler-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Toggle navigation</span>
        </button>

        <!-- Menu -->
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#"
                >Home</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Features</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Pricing</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Contact</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <div class="container my-3">
        <h2>Add a To-Do</h2>
        <form>
  <div class="mb-3">
    <label for="todotitle" class="form-label">Todo Title</label>
    <input type="text" class="form-control" id="todotitle" aria-describedby="title">
  </div>
  <div class="mb-3">
    <label for="desc" class="form-label">Todo Description</label>
    <input type="text" class="form-control" id="desc">
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
    </div>

    <div class="container my-4">
        <h2>Your To-Do List</h2>
        <table class="table">
  <thead>
    <tr>
      <th scope="col">S.No</th>
      <th scope="col">Title</th>
      <th scope="col">Description</th>
      <th scope="col">Date Created</th>
    </tr>
  </thead>
  <tbody>
    {% for todo in allTodo %}
    <tr>
      <th scope="row">{{loop.index}}</th>
      <td>{{todo.title}}</td>
      <td>{{todo.desc}}</td>
      <td>{{todo.date_created}}</td>
    </tr>
    {% endfor %}

  </tbody>
</table>
    </div>
    <!-- Bootstrap JS -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
    ></script>
  </body>
</html>
```

you can directly copy the index.html also from here after that go to `http://127.0.0.1:8000/`
our website will be like this:

<img width="1917" height="898" alt="image" src="https://github.com/user-attachments/assets/69c54ca1-cd16-441a-b7c9-316286076aa3" />

---

### **Step 6: Getting forms working**

- Now our data is all set but our form (Add a To-Do section) is not working so we will make it work

- I. Modify form in `index.html`:
  ```
      <form action="/" method="POST">
        <div class="mb-3">
          <label for="todotitle" class="form-label">Todo Title</label>
          <input
            type="text"
            class="form-control"
            id="todotitle"
            name="title"
            aria-describedby="title"
          />
        </div>
        <div class="mb-3">
          <label for="desc" class="form-label">Todo Description</label>
          <input type="text" class="form-control" name="desc" id="desc" />
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
  ```

- II. Modify `@app.route('/home')` in `app.py`:

```
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title="First Todo", desc="Start investing in Stock Market")
        db.session.add(todo)
        db.session.commit()
        
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)
```

Now go to Todo website and try adding something 

Example:

<img width="300" height="224" alt="image" src="https://github.com/user-attachments/assets/7c10c4e4-ad37-40cb-be22-953733ae4939" />

click submit and you will see it's added at S.no 8:

<img width="847" height="676" alt="image" src="https://github.com/user-attachments/assets/b34ce56b-2ccb-4549-b235-da74ea1b343f" />

- III. Now we will add a new table header Actions for update and delete a data

so we will modify table in `index.html`:
```
    <div class="container my-4">
      <h2>Your To-Do List</h2>
      <table class="table">
        <thead>
          <tr>
            <th scope="col">S.No</th>
            <th scope="col">Title</th>
            <th scope="col">Description</th>
            <th scope="col">Date Created</th>
            <th scope="col">Actions</th>
          </tr>
        </thead>
        <tbody>
          {% for todo in allTodo %}
          <tr>
            <th scope="row">{{loop.index}}</th>
            <td>{{todo.title}}</td>
            <td>{{todo.desc}}</td>
            <td>{{todo.date_created}}</td>
            <td>
              <a href="/update/{{todo.sno}}" type="button" class="btn btn-outline-success btn-sm mx-1">Update</a>
              <a href="/delete/{{todo.sno}}" type="button" class="btn btn-outline-danger btn-sm mx-1">Delete</a>
            </td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
```

now our todo app looks much better

<img width="1902" height="892" alt="image" src="https://github.com/user-attachments/assets/fb20c9cb-8bcd-4e5b-92e3-7cc9c9b0e580" />

---

### **Step 7: CRUD Operations**

✅ Add To-Do

✅ Show To-Do

✅ Update To-Do

✅ Delete To-Do

modify `app.py`:

```
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


# ---- CREATE DATABASE AUTOMATICALLY ----
with app.app_context():
    db.create_all()
# ---------------------------------------


# ----------------- HOME + ADD -----------------
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']

        # FIXED: use form values, not hard-coded strings
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()

        return redirect('/')  # refresh page after submit

    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)


# ----------------- DELETE -----------------
@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.get_or_404(sno)
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')


# ----------------- UPDATE -----------------
@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    todo = Todo.query.get_or_404(sno)

    if request.method == 'POST':
        todo.title = request.form['title']
        todo.desc = request.form['desc']
        db.session.commit()
        return redirect('/')

    return render_template('update.html', todo=todo)


# ------------------------------------------------

@app.route('/home')
def products():
    return "this is home page"


if __name__ == "__main__":
    app.run(debug=True, port=8000)
```

### You now need one more file: `update.html`

create **templates/update.html**

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Update Todo</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="container my-5">

  <h2>Update Todo</h2>

  <form action="/update/{{todo.sno}}" method="POST">
    <div class="mb-3">
      <label for="title" class="form-label">Title</label>
      <input id="title" type="text" class="form-control" name="title" value="{{todo.title}}" title="Title" placeholder="Enter title">
    </div>

    <div class="mb-3">
      <label for="desc" class="form-label">Description</label>
      <input id="desc" type="text" class="form-control" name="desc" value="{{todo.desc}}" title="Description" placeholder="Enter description">
    </div>

    <button class="btn btn-success" type="submit">Update</button>
    <a href="/" class="btn btn-secondary">Cancel</a>
  </form>

</body>
</html>
```
---

Now our website supports all CRUD Operations

**GET** - Get data

<img width="972" height="534" alt="image" src="https://github.com/user-attachments/assets/737fcecb-9b06-4140-898a-eda596277983" />

---

**POST** - Add data

<img width="970" height="525" alt="image" src="https://github.com/user-attachments/assets/9c41dec3-8a9c-4618-9d6b-6066fc05bfdb" />

---

**PUT** - Update data

<img width="843" height="317" alt="image" src="https://github.com/user-attachments/assets/d442720b-2e49-4283-bdfe-a197f4ccd9b2" />

Now it's updated

<img width="968" height="514" alt="image" src="https://github.com/user-attachments/assets/294cbac6-7319-4e86-968e-ddb5eb6be04a" />

---

**DELETE** - Delete data

<img width="970" height="490" alt="image" src="https://github.com/user-attachments/assets/5dd7f7b9-bd3f-427d-adc5-09b524a1331e" />

---

### Here are the modifications made for CRUD Operations and all so far:

**1. Enabled POST handling on the home route**
- Changed the `/` route to accept both GET and POST so form data can be submitted.

**2. Fixed todo creation**
- Replaced hard-coded values with the actual form inputs (`title` and `desc`).

**3. Added redirect after form submission**
- Redirects to `/` to avoid duplicate submissions and refresh cleanly.

**4. Added delete functionality**

- Created `/delete/<sno>` route that finds the todo by ID and deletes it.

**5. Added update functionality**

- Created `/update/<sno>` route to show an update form and save edited values.

**6. Created `update.html` template**

- Displays current todo values and allows editing.

**7. Adjusted homepage render**

- Sends `allTodo` list to `index.html` so the table displays all todos.

**8. Kept automatic database creation**

- Kept `db.create_all()` inside `app.app_context()` so tables are created automatically.


---

### **Step 8: Creating a base template**

**NOTE:**
Template inheritance means you create one main HTML file (a base template) with common parts like navbar, header, and footer, and other pages extend it. This way, you reuse the same layout everywhere without repeating code.

Now create one file **base.html** in `templates/`:

we will cut the code from `index.html` that we want it to remain fixed or common when navigationg to different page in our website:

**base.html**:
```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My Todo</title>

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" />
</head>

<body>
        <nav class="navbar navbar-expand-lg bg-primary" data-bs-theme="dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">My Todo App</a>

        <!-- Toggler -->
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-label="Toggle navigation"
          title="Toggle navigation"
        >
          <span class="navbar-toggler-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Toggle navigation</span>
        </button>

        <!-- Menu -->
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Features</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Pricing</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Contact</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
{% block body %}
    
{% endblock  body %}
</body>

</html>
```

modify **index.html**:
```
{% extends 'base.html' %}
{% block body %}

    <div class="container my-3">
      <h2>Add a To-Do</h2>
      <form action="/" method="POST">
        <div class="mb-3">
          <label for="todotitle" class="form-label">Todo Title</label>
          <input
            type="text"
            class="form-control"
            id="todotitle"
            name="title"
            aria-describedby="title"
          />
        </div>
        <div class="mb-3">
          <label for="desc" class="form-label">Todo Description</label>
          <input type="text" class="form-control" name="desc" id="desc" />
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </div>

    <div class="container my-4">
      <h2>Your To-Do List</h2>
      <table class="table">
        <thead>
          <tr>
            <th scope="col">S.No</th>
            <th scope="col">Title</th>
            <th scope="col">Description</th>
            <th scope="col">Date Created</th>
            <th scope="col">Actions</th>
          </tr>
        </thead>
        <tbody>
          {% for todo in allTodo %}
          <tr>
            <th scope="row">{{loop.index}}</th>
            <td>{{todo.title}}</td>
            <td>{{todo.desc}}</td>
            <td>{{todo.date_created}}</td>
            <td>
              <a href="/update/{{todo.sno}}" type="button" class="btn btn-outline-success btn-sm mx-1">Update</a>
              <a href="/delete/{{todo.sno}}" type="button" class="btn btn-outline-danger btn-sm mx-1">Delete</a>
            </td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>

{% endblock  body %}
```


---

### **Step 9: Deploying our To-Do App on Heroku**

Follow these commands:
```
heroku login

pip install gunicorn
pip freeze requirements.txt
Procfile
web: gunicorn app:app

git init
git add .
git commit -m "Initial commmit"

heroku create todo-tejax
git remote -v
git push heroku master
```




⭐ Now it's all done!! ⭐

---

## 3. RESOURCES

Flask Official Documentation: [Flask](https://flask.palletsprojects.com/en/stable/)

Flask-SQLAlchemy Documentation: [Flask-SQLAlchemy](https://flask-sqlalchemy.readthedocs.io/en/stable/)

Heroku Deployment Guide: [Heroku Deployment](https://coding-boot-camp.github.io/full-stack/heroku/heroku-deployment-guide)

---

<h3 align="center">✨ <strong>Happy Coding ✨</strong> </h3>

