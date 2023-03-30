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
        print("Hello! Welcome to *Reviewer*")
        print('')
        print('''
                 _v_              _v_  
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
                0 - Quit Program

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
    student = session.query(Student).filter_by(name=student_name.title()).first()
    if student and student_program_password == "password":
        student_page(student)
    else:
        print("No name found - Please re-enter Name.")
        student_login_page()

def student_page(student):
    page_num = 3
    student_menu_choice = int(input(f'''
            Hi {student.name}!
            
            Please select:
            1 - Write a Review
            2 - See Reviews you have Written
            3 - Edit your Review
            4 - Update your Phone Number or Email
            5 - Delete a Review
            6 - Create new Profile (coming soon!!)
            7 - Go Back
            0 - Quit Program

            ENTER: '''))
    if student_menu_choice == 1:
        student_write_reivew(student)

    elif student_menu_choice == 2:
        print('please work 3')
        view_student_reviews(student)

#     elif student_menu_choice == 3:
#         print('please work 4')
        
#     elif student_menu_choice == 4:
#         print('please work 5')

#     elif student_menu_choice == 5:
#         print('please work 6')

#     elif student_menu_choice == 6:
#         print('please work 7')

#     elif student_menu_choice == 7:
#         main_menu()

    elif student_menu_choice == 8:
        student_page = 0
        
    else:
        print("Invalid selection. Please try again.")

def student_write_reivew(student):
    print('')
    student_review = str(input("Write your Honest Review: "))
    student_rating = float(input("Leave your Honest Rating of the Program (1-5): "))

    review = Review(student_id=student.id, program=student.program, comment=student_review, rating=student_rating)

    session.add(review)
    session.commit()

    print('Thank you for Submitting a Review!')
    student_page(student)

def view_student_reviews():
    reviews = session.query(Review).filter_by(student_id=student.id).all()
    pass
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
#                 0 - Quit Program

#                 ENTER: '''))

#### FOR BOTH TEACHERS AND STUDENTS:
def create_reviews_table(reviews):
    table = PrettyTable()
    table.title = ' 📝 REVIEWS 📝'
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
#                  _v_              _v_  
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
#                 0 - Quit Program

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
    teacher_name = str(input("Enter Your Name:  "))
    teacher_password = str(input("Enter Your Employee Password: "))
    teacher = session.query(Teacher).filter_by(name=teacher_name.title()).first()
    if teacher and teacher_password == "flatsteel school":
        teacher_page(teacher)
    else:
        print("No Record Found - Please Re-Enter Your Name and Password")
        teacher_login_page()

def teacher_page(teacher):
    teacher_page = 0
    if teacher_page == 0:
        choice = int(input(f'''
                Hi {teacher.name}!

                Please select:
                1 - See Reviews
                2 - Write a New Review
                3 - Delete Your Review(s)
                4 - Update Your Review
                5 - Go Back
                0 - Quit Program

                ENTER: '''))
        if choice == 1:
            teacher_page = 1
            teacher_reviews(teacher)
        elif choice == 2:
            teacher_page = 1
            teacher_write_review(teacher)
        elif choice == 3:
            teacher_page = 1
            teacher_delete(teacher)
        elif choice == 4:
            teacher_page = 1
            teacher_update()
        elif choice == 5:
            teacher_page = 1
            main_menu()
        elif choice == 0:
            teacher_page = 0

def teacher_reviews(teacher):
    teacher_review_page = 0
    if teacher_review_page == 0:
        reviews = session.query(Review)
        create_reviews_table(reviews)
        choice = int(input(f'''

                Please select:
                1 - Filter By Program
                2 - See Your Reviews
                3 - Go Back
                0 - Quit Program

                ENTER: '''))
        
        if choice == 1:
            teacher_review_page = 1
            chosen_program = str(input("Please Input Program Name: "))
            review_list = [review for review in reviews if review.program.lower() == chosen_program.lower()] 
            create_reviews_table(review_list)
            prompt = str(input("Would you Like to See More? [ yes / no ]:  "))
            if prompt in YES:
                teacher_reviews(teacher)
            else: 
                print("Thanks for Visiting!")
        elif choice == 2:
            teacher_review_page = 1
            review_list = [review for review in reviews if review.teacher_id == teacher.id] 
            create_reviews_table(review_list)
            prompt = str(input("Would you Like to See More? [ yes / no ]:  "))
            if prompt in YES:
                teacher_reviews(teacher)
            else: 
                print("Thanks for Visiting!")
        elif choice == 3:
            teacher_review_page = 1
            teacher_page(teacher)
        elif choice == 0:
            teacher_review_page = 0


# https://pypi.org/project/prettytable/
# python -m pip install -U prettytable

def teacher_write_review(teacher):
    print('')
    teacher_review = str(input("Write your Honest Review: "))
    teacher_rating = float(input("Leave your Honest Rating of the Program (1-5): "))

    review = Review(teacher_id=teacher.id, program=teacher.program, comment=teacher_review, rating=teacher_rating)

    session.add(review)
    session.commit()

    print('Thank you for Submitting a Review!')
    teacher_page(teacher)

def teacher_delete(teacher):
    teacher_review_page = 0
    if teacher_review_page == 0:
        reviews = session.query(Review)
        review_list = [ review for review in reviews if review.teacher_id == teacher.id] 
        create_reviews_table(review_list)
        if len(review_list) == 0:
            "You Have Not Written a Review Yet!"
        prompt = str(input("Would You Like to Return to the Main Menu? [ yes / no ]:  "))
        if prompt in YES:
            teacher_page(teacher)
        else: 
            print("Thanks for Visiting!")
        
    

def teacher_update():
    pass


    