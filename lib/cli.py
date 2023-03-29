from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Student, Teacher, Review

from helpers import main_menu, student_login_page, student_page

engine = create_engine('sqlite:///db/reviews.db')
session = sessionmaker(bind=engine)

if __name__ == '__main__':
    main_menu()




# log in feature for students / stretch goals
    # password to access student/ teacher portal:

# main menu: (already made) / stretch goals - individual profile
    # if student - student log in portal
    # if teacher - teacher log in portal

# Students:
    # write a review (CREATE)
        # identify yourself feature
    # see their own reviews (using Student.name?) (READ)
        # table - prettytable
    # update their information/ review (UPDATE)
    # delete their review (DELETE)
    # create profile (CREATE)




# SAKI







# HENRY

    