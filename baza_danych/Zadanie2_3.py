from sqlalchemy import create_engine, Column, Integer, String, Float, text
from sqlalchemy.orm import declarative_base, Session


engine = create_engine('sqlite+pysqlite:///:memory:', echo=True, future=True)
Base = declarative_base()


#Zadanie 2
#definicja klasy
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    grade = Column(Float)

    def dodajStudenta(self, name, age, grade):
        with Session(engine) as session:
            new_student = Student(name=name, age=age, grade = grade)
            session.add(new_student)
            session.commit()
    def daneStudentaPoID(self, id):
        with Session(engine) as session:
            student_by_id = session.get(Student, id)
            print(f'{student_by_id.name}, {student_by_id.age}, {student_by_id.grade}')

    def aktualizacjaDanych(self, id):
        with Session(engine) as session:
            student_by_id = session.get(Student, id)
            if student_by_id:
                name = input("Podaj imie do zmiany")
                student_by_id.name = name
                age = input("Podaj wiek do zmiany")
                student_by_id.age = age
                grade = input("Podaj ocenę do zmiany")
                student_by_id.age = grade
                session.commit()
    def usunStudenta(self,id):
        with Session(engine) as session:
            student_to_delete = session.get(Student, id)
            if student_to_delete:
                session.delete(student_to_delete)
                session.commit()

# Tworzenie wszystkich tabel
Base.metadata.create_all(engine)


with Session(engine) as session:
    new_student1 = Student(name="Jan Kowalski", age=30, grade=4.0)
    new_student2 = Student(name="Jan Nowak", age=25, grade=3.0)
    new_student3 = Student(name="Jan Michalak", age=45, grade=5.0)
    session.add(new_student1)
    session.add(new_student2)
    session.add(new_student3)
    session.commit()


# oeczyt danych z sesji
with (Session(engine) as session):
    students = session.execute(text("SELECT * FROM students")).all()
    for student in students:
        print(f'{student.name}, {student.age}, {student.grade}')


# Usuwanie rekordy z bazy
with Session(engine) as session:
    for i in range(1,4):
        student_to_delete = session.get(Student, i)
        if student_to_delete:
            session.delete(student_to_delete)
            session.commit()

#Sprawdzenie czy zostali jeszcze jacyś studenci w bazie
with (Session(engine) as session):
    students = session.execute(text("SELECT * FROM students")).all()
    for student in students:
        print(f'{student.name}, {student.age}, {student.grade}')


#Zadanie 3

