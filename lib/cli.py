from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Student, Teacher, Review

from helpers import next_page

engine = create_engine('sqlite:///db/reviews.db')
session = sessionmaker(bind=engine)

YES = ['y', 'ye', 'yes']
NO = ['n','no']
line = '-'*50 #adds line
line_db = '\n' + line + '\n' #adds line with double spacing

if __name__ == '__main__':
    print('')
    print("Hello! Thank you for taking the time to write a review!")
    print('')
    print('''
              ___              ___  
             (o o)            (o o) 
            (  V  ) Reviewer (  V  )
            --m-m--------------m-m--
    ''')

    page = 1
    # main_menu = True
    if page == 1:

        # task_selection = True

        identity = int(input(f'''
    Please select which one you are:
    1 - Student
    2 - Teacher
    3 - End the Program

    ENTER: '''))
        if identity == 1:
            page = 2
            next_page()

            # if page == 2:
            #     print("student page!")
        elif identity == 2:
            print('please work')
            # print("Hi teacher!")
            # page += 10
            # if page == 11:
            #     print("teacher page!")
        elif identity == 3:
            page = 0
        else:
            print("Invalid selection. Please try again.")

    #if task_selection == False:
        #then this_func()

    #this_func()




    