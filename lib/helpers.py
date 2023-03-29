from db.models import Student, Teacher, Review

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from prettytable import PrettyTable
# import re

engine = create_engine('sqlite:///db/reviews.db')
Session = sessionmaker(bind=engine)
session = Session()

YES = ['Y', 'y', 'ye', 'yes']
NO = ['N', 'n','no']
# line = '-'*50 
#adds line
# line_db = '\n' + line + '\n' 
#adds line with double spacing


def main_menu():
        print('')
        print("Hello! Thank you for taking the time to write a review!")
        print('')
        print('''
                 ___              ___  
                (o o)            (o o) 
               (  V  ) Reviewer (  V  )
               --m-m--------------m-m--
        ''')

        page_num = 1
        if page_num == 1:

            identity = int(input(f'''
                Please select which one you are:
                1 - Student
                2 - Teacher
                3 - Quit Program

                ENTER: '''))
            if identity == 1:
                page_num = 2
                student_login_page()

            elif identity == 2:
                page_num = 3
                teacher_login_page()

            elif identity == 3:
                page_num = 0
            else:
                print("Invalid selection. Please try again.")

def student_login_page():
    page_num = 2
    student_name = str(input("Enter your Name: "))
    student_program_password = str(input("Enter your Program Password: "))
    student = session.query(Student).filter_by(name=student_name).first()
    if student and student_program_password == "password":
        student_page()
    else:
        print("No name found - Please re-enter Name.")
        student_login_page()

def student_page():
    page_num = 3
    student_menu_choice = int(input(f'''
            Please select:
            1 - Write a Review
            2 - See Reviews you have Written
            3 - Edit your Review
            4 - Update your Phone Number or Email
            5 - Delete a Review
            6 - Create new Profile (coming soon!!)
            7 - Go Back
            8 - Quit Program

            ENTER: '''))
    if student_menu_choice == 1:
        student_page = 2
        student_write_reivew()

    elif student_menu_choice == 2:
        student_page = 3
        print('please work 3')

#     elif student_menu_choice == 3:
#         student_page = 4
#         print('please work 4')
        
#     elif student_menu_choice == 4:
#         student_page = 5
#         print('please work 5')

#     elif student_menu_choice == 5:
#         student_page = 6
#         print('please work 6')

#     elif student_menu_choice == 6:
#         student_page = 7
#         print('please work 7')

#     elif student_menu_choice == 7:
#         main_menu()

#     elif student_menu_choice == 8:
#         student_page = 0
        
#     else:
#         print("Invalid selection. Please try again.")

def student_write_reivew():
    student_page = 2
    print('')
    student_review = str(input("Write your Honest Review: "))
#     review = 

# def view_student_reviews():
#     teacher_review_page = 1
#     if teacher_review_page == 1:
#         reviews = session.query(Review)
#         create_reviews_table(reviews)
#         # print(table)
#         choice = int(input(f'''
#                 Please select:
#                 1 - Filter By Program
#                 2 - See Your Reviews
#                 3 - Go Back
#                 4 - Quit Program

#                 ENTER: '''))

#### FOR BOTH TEACHERS AND STUDENTS:
def create_reviews_table(reviews):
    table = PrettyTable()
    table.title = ' REVIEWS '
    table.field_names = ['Student ID', 'Teacher ID', 'Comment', 'Rating', 'Date', 'Program']
    for review in reviews:
        table.add_row([
            review.student_id,
            review.teacher_id,
            review.comment,
            review.rating,
            review.date.strftime('%Y-%m-%d'),
            review.program
        ])
    print(table)

# SAKI

# Teachers:
    # see all reviews
        # table 
        # filter by:
            # program name + average rating (table)
            # reviews they have written
    # write a review
    # delete their own reviews
    # update their reviews
    # ( add student to a program )

# def main_menu():
#         print('')
#         print("Hello! Thank you for taking the time to write a review!")
#         print('')
#         print('''
#                  ___              ___  
#                 (o o)            (o o) 
#                (  V  ) Reviewer (  V  )
#                --m-m--------------m-m--
#         ''')

#         page_num = 1
#         if page_num == 1:

#             identity = int(input(f'''
#                 Please select which one you are:
#                 1 - Student
#                 2 - Teacher
#                 3 - Quit Program

#                 ENTER: '''))
#             if identity == 1:
#                 page_num = 2
#                 student_login_page()

#             elif identity == 2:
#                 page_num = 3
#                 teacher_login_page()

#             elif identity == 3:
#                 page_num = 0
#             else:
#                 print("Invalid selection. Please try again.")
    
def teacher_login_page():
    teacher_login_page = 1
    if teacher_login_page == 1:
        teacher_name = str(input("Enter Your Name:  "))
        teacher_password = input("Enter Your Employee Password: ")
        teacher_id = session.query(Teacher).filter_by(name=teacher_name).first().id
        if teacher_id and teacher_password == "flatsteel school":
            teacher_login_page = 2
            teacher_page()
        else:
            print("No Name Found - Please Re-Enter Your Name")
            teacher_login_page()

def teacher_page():
    teacher_page = 1
    if teacher_page == 1:
        choice = int(input(f'''
                Please select:
                1 - See All Reviews
                2 - Write a New Review
                3 - Delete Your Review
                4 - Update Your Review
                5 - Go Back
                6 - Quit Program

                ENTER: '''))
        if choice == 1:
            teacher_page = 2
            teacher_reviews()
        elif choice == 2:
            teacher_page = 2
            teacher_write_review()
        elif choice == 3:
            teacher_page = 3
            teacher_delete()
        elif choice == 4:
            teacher_login_page()
        elif choice == 5:
            main_menu()
        elif choice == 6:
            teacher_page = 0

def teacher_reviews():
    teacher_review_page = 1
    if teacher_review_page == 1:
        reviews = session.query(Review)
        create_reviews_table(reviews)
        # print(table)
        choice = int(input(f'''
                Please select:
                1 - Filter By Program
                2 - See Your Reviews
                3 - Go Back
                4 - Quit Program

                ENTER: '''))

# https://pypi.org/project/prettytable/
# python -m pip install -U prettytable

def teacher_write_review():
    pass

def teacher_delete():
    pass

def teacher_update():
    pass


    