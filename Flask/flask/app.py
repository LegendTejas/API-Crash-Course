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