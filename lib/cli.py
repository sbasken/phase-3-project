from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Student, Teacher, Review

#from helpers import 

engine = create_engine('sqlite:///db/reviews.db')
session = sessionmaker(bind=engine)

YES = ['y', 'ye', 'yes']
NO = ['n','no']
line = '-'*50 #adds line
line_db = '\n' + line + '\n' #adds line with double spacing

if __name__ == '__main__':
    print("Hello! Thank you for taking the time to write a review!")
    print('')