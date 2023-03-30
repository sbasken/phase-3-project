from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Student, Teacher, Review

from helpers import main_menu, student_login_page, student_page

engine = create_engine('sqlite:///db/reviews.db')
session = sessionmaker(bind=engine)

if __name__ == '__main__':
    main_menu()



    