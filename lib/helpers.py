from db.models import Student, Teacher


def next_page():
    choice = int(input(f'''
        Please select:
        1 - View Student Records
        2 - Add Student
        3 - Quit Program

    ENTER: '''))
    if choice == 1:
            page = 2
            print("hi")

            # if page == 2:
            #     print("student page!")
    elif choice == 2:
        print('please work')
        # print("Hi teacher!")
        # page += 10
        # if page == 11:
        #     print("teacher page!")
    elif choice == 3:
        page = 0
    else:
        print("Invalid selection. Please try again.")