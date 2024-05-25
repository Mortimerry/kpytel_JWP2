from flask import Flask, render_template, request, redirect, url_for
from models import db, Teacher

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teachers.db'
db.init_app(app)

@app.route('/')
def index():
    teachers= Teacher.query.all()
    return render_template('index.html', teachers=teachers)

@app.route('/add', methods=['POST'])
def addTeacher():
    name = request.form.get('name')
    subject = request.form.get('subject')
    time = request.form.get('time')
    if name and subject and time:
        new_teacher= Teacher(name=name, subject = subject, time = time)
        db.session.add(new_teacher)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:teacher_id>')
def deleteTeacher(teacher_id):
    teacher = Teacher.query.get(teacher_id)
    if teacher:
        db.session.delete(teacher)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0')