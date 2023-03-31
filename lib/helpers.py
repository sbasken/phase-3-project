from db.models import Student, Teacher, Review

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from prettytable import PrettyTable
import time

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
        print('')
        print('''
              Hello! Welcome to Reviewer!

                 _v_              _v_  
                (o o)            (o o) 
               (  V  ) Reviewer (  V  )
               --m-m--------------m-m--
        ''')

        page_num = 1
        try:
            if page_num == 1:

                identity = int(input(f'''
                Please select which one you are:
                1 - Student
                2 - Teacher
                3 - Create New Student Profile
                4 - Create New Teacher Profile
                0 - Quit Program

                ENTER: '''))
                if identity == 1:
                    page_num = 2
                    student_login_page()

                elif identity == 2:
                    page_num = 3
                    teacher_login_page()

                elif identity == 3:
                    page_num = 4
                    create_new_student_profile()
                
                elif identity == 4:
                    page_num = 5
                    create_new_teacher_profile()

                elif identity == 0:
                    page_num = 0
                else:
                    print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid selection. Please input one of the options presented above.")
            time.sleep(2)
            main_menu()

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
    try:
        student_menu_choice = int(input(f'''
                Hi {student.name}!
                
                Please select:
                1 - Write a Review
                2 - See Reviews you have Written
                3 - Edit your Review
                4 - Update your Phone Number or Email
                5 - Delete a Review
                6 - Go Back
                0 - Quit Program

                ENTER: '''))
        if student_menu_choice == 1:
            print("navigating to desired page")
            time.sleep(1)
            student_write_reivew(student)

        elif student_menu_choice == 2:
            print("navigating to desired page")
            time.sleep(1)
            view_student_reviews(student)

        elif student_menu_choice == 3:
            print("navigating to desired page")
            time.sleep(1)
            edit_student_reviews(student)
            
        elif student_menu_choice == 4:
            print("navigating to desired page")
            time.sleep(1)
            update_email_or_pn(student)

        elif student_menu_choice == 5:
            print("navigating to desired page")
            time.sleep(1)
            delete_selected_review(student)

        elif student_menu_choice == 6:
            print("navigating to desired page")
            time.sleep(1)
            main_menu()

        elif student_menu_choice == 0:
            print("Bye! Thanks for visiting! Hope to see you again soon!")
            time.sleep(1)
            page_num = 0
            
        else:
            print("Invalid selection. Please try again.")
    except ValueError:
        print("Invalid selection. Please input one of the options presented above.")
        time.sleep(2)
        student_page(student)

def student_write_reivew(student):
    print('''
 ^ ^                                 
(O,O)                                
(   ) Thank you for taking the time to leave feedback!    
-"-"---------------------------------------------------
''')
    student_review = str(input("Write your Honest Review: "))
    student_rating = float(input("Leave your Honest Rating of the Program (1-5): "))

    review = Review(student_id=student.id, program=student.program, comment=student_review, rating=student_rating)

    session.add(review)
    session.commit()

    print('Thank you for Submitting a Review!')
    student_page(student)

def view_student_reviews(student):
    written_student_reviews = session.query(Review).filter_by(student_id=student.id).all()
    if written_student_reviews:
        create_reviews_table(written_student_reviews)
        student_menu = str(input("Finished looking? Would you like to head back to the Main Menu? (Type Y/N): "))
        if student_menu in YES:
            student_page(student)
        elif student_menu in NO:
            print("Take your Time!")
        else:
            print("Please input YES or NO.")
            time.sleep(2)
            view_student_reviews(student)
    else:
        print("You have no reviews yet! Write one to show it here!")
        time.sleep(1)
        student_page(student)

def edit_student_reviews(student):
    reviews = session.query(Review).filter_by(student_id=student.id).all()
    if not reviews:
        print("You have no reviews to edit!")
        student_page(student)
    else:
        create_reviews_table(reviews)
        review_choice = int(input("Enter the number of the review you want to edit (or 0 to go back): "))
        if review_choice == 0:
            student_page(student)
        elif review_choice > len(reviews):
            print("Invalid selection. Please try again.")
            edit_student_reviews(student)
        else:
            selected_review = reviews[review_choice - 1]
            new_comment = input("Enter your new comment: ")
            new_rating = float(input("Enter your new rating (1-5) "))
            selected_review.comment = new_comment
            selected_review.rating = new_rating

            session.commit()
            print("Review updated successfully!")
            student_page(student)

def update_email_or_pn(student):
    current_student = session.query(Student).filter_by(id=student.id).first()
    try:
        info_change_selection = int(input('''
                Which one would you like to update?
                    1 - Email
                    2 - Phone Number
                    3 - Go Back
                ENTER: '''))
        if info_change_selection == 1:
            email_change = str(input("New Email: "))
            current_student.email = email_change

            session.commit()
            print("Information successfully updated!")
            time.sleep(1)
            student_page(student)

        elif info_change_selection == 2:
            phone_number_change = int(input("New Phone Number: "))
            formatted_phone_number = "({}) {} - {}".format(str(phone_number_change)[0:3], str(phone_number_change)[3:6], str(phone_number_change)[6:])
            current_student.phone_number = formatted_phone_number

            session.commit()
            print("Information successfully updated!")
            time.sleep(1)
            student_page(student)

        elif info_change_selection == 3:
            student_page(student)
        else:
            print("Invalid Selection. Please input 1 or 2.")

        # session.commit()
        # print("Information successfully updated!")
    except ValueError:
        print("Invalid selection. Please input one of the options presented above.")
        time.sleep(2)
        update_email_or_pn(student)
    
    # session.commit()
    # print("Information successfully updated!")
    # student_page(student)

def delete_selected_review(student):
    reviews = session.query(Review).filter_by(student_id=student.id).all()
    if not reviews:
        print("You have no reviews to delete!")
        time.sleep(1)
        student_page(student)
    else:
        create_reviews_table(reviews)
        review_choice = int(input("Enter the number of the review you want to delete (or 0 to go back): "))
        if review_choice == 0:
            student_page(student)
        elif review_choice > len(reviews):
            print("Invalid selection. Please try again.")
            time.sleep(1)
            delete_selected_review(student)
        else:
            selected_review = reviews[review_choice - 1]
            session.delete(selected_review)
            session.commit()
            print("Review successfully deleted!")
            time.sleep(1)
            student_page(student)


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
    teacher_nav_page = 1
    try:
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
            teacher_nav_page = 2
            teacher_reviews(teacher)
        elif choice == 2:
            teacher_nav_page = 3
            teacher_write_review(teacher)
        elif choice == 3:
            teacher_nav_page = 4
            teacher_delete_page(teacher)
        elif choice == 4:
            teacher_nav_page = 5
            teacher_update_review(teacher)
        elif choice == 5:
            teacher_nav_page = 6
            main_menu()
        elif choice == 0:
            teacher_nav_page = 0
    except ValueError:
        print("Invalid selection. Please input one of the options presented above.")
        time.sleep(2)
        teacher_page(teacher)

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

def teacher_delete_page(teacher):
    teacher_review_page = 0
    if teacher_review_page == 0:
        reviews = session.query(Review)
        review_list = [ review for review in reviews if review.teacher_id == teacher.id] 
        if len(review_list) == 0:
            print("")
            print("You Have No Review Yet!")
            prompt = str(input("Would You Like to Return to the Main Menu? [ yes / no ]:  "))
            if prompt in YES:
                teacher_page(teacher)
            else: 
                print("Thanks for Visiting!")
        else:
            create_reviews_table(review_list)
            prompt = str(input("Would You Like to Delete Your Review(s)? [ yes / no ]:  "))
            if prompt in YES:
                review_choice = int(input("Enter the number of the review you want to delete (or 0 to go back): "))
                if review_choice == 0:
                    teacher_page(teacher)
                elif review_choice > len(reviews):
                    print("Invalid selection. Please try again.")
                    teacher_delete_page(teacher)
                else:
                    selected_review = reviews[review_choice - 1]
                    session.delete(selected_review)
                    session.commit()
                    print("Review successfully deleted!")
                    teacher_page(teacher)
            else: 
                print("Thanks for Visiting!")
            
    

def teacher_update_review(teacher):
    reviews = session.query(Review).filter_by(teacher_id=teacher.id).all()
    if not reviews:
        print("You have no reviews to edit!")
        teacher_page(teacher)
    else:
        create_reviews_table(reviews)
        review_choice = int(input("Enter the number of the review you want to edit (or 0 to go back): "))
        if review_choice == 0:
            teacher_page(teacher)
        elif review_choice > len(reviews):
            print("Oops! This is an invalid selection. Please try again.")
            teacher_update_review(teacher)
        else:
            selected_review = reviews[review_choice - 1]
            new_comment = input("Enter your new comment: ")
            new_rating = float(input("Enter your new rating (1-5): "))
            selected_review.comment = new_comment
            selected_review.rating = new_rating

            session.commit()
            print("Review updated successfully!")
            teacher_page(teacher)


    
# NEW PROFILE CREATION FUNCTIONS:

def create_new_student_profile():
    name = str(input("Please Enter your Full Name: "))
    program = str(input("Program you are Currently Enrolled in: "))
    email = str(input("Please enter your Email: "))
    phone_number_change = int(input("New Phone Number: "))
    formatted_phone_number = "({}) {} - {}".format(str(phone_number_change)[0:3], str(phone_number_change)[3:6], str(phone_number_change)[6:])
    student = Student(name=name, program=program, email=email, phone_number=formatted_phone_number)

    session.add(student)
    session.commit()
    print('''
        Welcome to Reviewer {}!
        We're really excited for you to join this community!

        As a student you have access to lots of cool features on this app!

        Feel free to look through and if you run into any issues/ questions -
        don't hesitate to reach out!

        Your password on login is: "password"

        Happy Coding!
    '''.format(name))

    print("Please wait as we are creating your profile!")
    time.sleep(10)

    main_menu()

def create_new_teacher_profile():
    name = str(input("Please Enter your Full Name: "))
    program = str(input("Program you are Currently Enrolled in: "))
    email = str(input("Please enter your Email: "))
    teacher = Teacher(name=name, program=program, email=email)

    session.add(teacher)
    session.commit()
    print('''
        Welcome {}!
        We're really excited for you to join this community!

        As a teacher you have full access to view all reviews across
        all programs! We hope that you can regularly read your own 
        reviews and report any/all issues students are running into
        back to the curriculum team so that this school can run 
        seamlessly and efficiently while also giving students the 
        best possible experience!

        Your password on login is: "flatsteel school"

        Happy Coding! and Please don't hesitate to reach out if
        there's anything we can support you with!
    '''.format(name))

    print("Please wait as we are creating your profile!")
    time.sleep(10)

    main_menu()