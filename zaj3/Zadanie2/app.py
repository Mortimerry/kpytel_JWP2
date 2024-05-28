from flask import Flask, render_template, request, redirect, url_for
from models import db, Task
import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['TEMPLATES_AUTO_RELOAD'] = True
db.init_app(app)

@app.route('/')
def index():
    tasks= Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def addTask():
    name = request.form.get('name')
    if name:
        new_task= Task(name=name)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for("index"))

@app.route('/delete/<int:task_id>')
def deleteTask(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('index'))

@app.route("/edit/<int:task_id>", methods=["POST"])
def editTask(task_id):
    task = Task.query.filter_by(id=task_id).first()
    updated_task = request.form.get("name")
    if updated_task:
        task.name = updated_task
        db.session.commit()
    return redirect(url_for("index"))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0')