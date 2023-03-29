from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Student, Teacher, Review

if __name__ == '__main__':
    engine = create_engine("sqlite:///db/reviews.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Student).delete()
    session.query(Teacher).delete()
    session.query(Review).delete()

    faker = Faker()

    programs = ['software engineering', 'data science', 'ux/ui', 'cyber security','machine learning', 'flex']

    students = []

    for _ in range(50):

        student = Student(
            name = f"{faker.first_name()} {faker.last_name()}",
            program = random.choice(programs),
            email = faker.email(),
            phone_number = f"({random.randint(100, 999)}) {random.randint(100, 999)} - {random.randint(1000, 9999)}"
        )
        
        session.add(student)
        session.commit()

        students.append(student)

    teachers = []

    for student in students:
        for _ in range(10):
            teacher = Teacher(
                name = f"{faker.first_name()} {faker.last_name()}",
                program = random.choice(programs),
                email = faker.email()
            )

            session.add(teacher)
            session.commit()

            teachers.append(teacher)
    
    
    reviews = []
    student_comments = ['I don\'t think I\'ll ever use this class in real life.', 'I would not recommend this class.', 'It was challenging, but I\'m glad I got through it!', 'I would take this class again if I could!', 'Best class ever!']
    teacher_comments = ['Need to work on attendance...', 'Curriculum team needs to work on the modules...', 'Testing file needs to be improved...', 'Modules missing some lessons', 'Good job!', 'Exhibited great perseverance', 'Great work but don\'t forget to take a break and rest!', 'Good attendance and engagement', 'Great work!', 'Had a great time teaching this class!',  'Excellent work!', 'Great team work', 'Excellent project and presentation', 'Student of the year!']
    reviewers = [ "student", "teacher" ] 
    # 0,1 = 1 / 2,3 = 2 / 4,5,6 = 3 / 7 = 4 / 8,9,10,11,12 = 5

    for _ in range(80):

        reviewed_by = random.choice(reviewers)
        comment = random.choice(student_comments)
        if reviewed_by == "student":

            if comment == student_comments[0]:
                rating = 1
            elif comment == student_comments[1]:
                rating = 2
            elif comment == student_comments[2]:
                rating = 3
            elif comment == student_comments[3]:
                rating = 4
            elif comment == student_comments[4]:
                rating = 5
        
            review = Review(
                student_id = random.choice(students).id,
                program = random.choice(programs),
                comment = comment,
                rating = rating,
                date = faker.date_this_year()
            )

            session.add(review)
            session.commit()
            reviews.append(review)

        else:
            comment = random.choice(teacher_comments)

            if comment in teacher_comments[:2]:
                rating = 1
            elif comment in teacher_comments[2:4]:
                rating = 2
            elif comment in teacher_comments[4:7]:
                rating = 3
            elif comment in teacher_comments[7:8]:
                rating = 4
            elif comment in teacher_comments[8:]:
                rating = 5
        
            review = Review(
                teacher_id = random.choice(teachers).id,
                program = random.choice(programs),
                comment = comment,
                rating = rating,
                date = faker.date_this_year()
            )

            session.add(review)
            session.commit()
            reviews.append(review)