from peewee import *

db = SqliteDatabase('students.db')

class Student(Model):
    username = CharField(max_length=255 ,unique=True)
    points = IntegerField(default=0)
    
    class Meta :                # este class meta define la tabla en la base de datos
        database = db
        
students = [
    {'username': 'john', 'points': 100},
    {'username': 'jane', 'points': 200},
    {'username': 'bob', 'points': 10},
    {'username': 'alice', 'points': 400},
    {'username': 'charlie', 'points': 5},
]

def add_students():
    for student in students:
        try:
            Student.create(username=student['username'], points=student['points'])
        except IntegrityError:
            student_record = Student.get(username=student['username'])
            student_record.points = student['points']
            student_record.save()
            
def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    return student
        
if __name__ == '__main__':
    db.connect()
    db.create_tables([Student],safe=True)  # Crea la tabla si no existe
    print('El mejor estudiante fue: {}'.format(top_student().username))  # imprime el nombre del estudiante con más puntos
    