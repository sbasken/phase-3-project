from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Student, Teacher, Review

if __name__ == '__main__':
    engine = create_engine("sqlite:///reviews.db")
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
            phone_number = random.randint(1000000000, 9999999999)
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
    student_comments = ['Best class ever!', 'It was challenging, but I\'m glad I got through it!', 'I would not recommend this class.', 'I don\'t think I\'ll ever use this class in real life.', 'I would take this class again if I could!']
    teacher_comments = ['Great work!', 'Need to work on attendance...', 'Good job!', 'Had a great time teaching this class!', 'Curriculum team needs to work on the modules...', 'Testing file needs to be improved...', 'Excellent work!', 'Great team work']
    reviewers = [ "student", "teacher" ] 

    for _ in range(80):

        reviewed_by = random.choice(reviewers)
        if reviewed_by == "student":
        
            review = Review(
                student_id = random.choice(students).id,
                # teacher_id= random.choice(teachers).id,
                comment = random.choice(student_comments),
                rating = random.randint(1,5),
                date = faker.date_this_year()
            )

            session.add(review)
            session.commit()
            reviews.append(review)

        else:
            review = Review(
                teacher_id= random.choice(teachers).id,
                comment = random.choice(teacher_comments),
                rating = random.randint(1,5),
                date = faker.date_this_year()
            )
            session.add(review)
            session.commit()
            reviews.append(review)