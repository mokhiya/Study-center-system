from Admin.superadmin import create_admin, check_super_admin, check_admin, verify_admins, send_message
from Admin.admin import show_admin_menu
from Student.studentmenu import check_student, show_student_menu
from Teacher.teachermenu import check_teacher, show_teacher_menu
from file_manager import admin_manager, teacher_manager, student_manager

super_admin_login = "admin"
super_admin_password = "0000"


def send_message_to_all():
    """
    This function sends a message to selected groups of users (admins, teachers, students) based on the user's choice.
    """
    topic = input("What do you want to send? >>> ").strip()
    text = input("""
    Whom do you want to send?
    1. To all admins.
    2. To all teachers.
    3. To all students.
    4. Only to female teachers.
    5. Only to female students.
    6. Only to male teachers.
    7. Only to male students.
    8. Go to back.

    Choose an option above: """)

    message = "Email is sent successfully."

    if text == '1':
        send_message('admins', admin_manager, topic)
        print(message)
    elif text == '2':
        send_message('teachers', teacher_manager, topic)
        print(message)
    elif text == '3':
        send_message('students', student_manager, topic)
        print(message)
    elif text == '4':
        send_message('teachers', teacher_manager, topic)
        print(message)
    elif text == '5':
        send_message('students', student_manager, topic)
        print(message)
    elif text == '6':
        send_message('teachers', teacher_manager, topic)
        print(message)
    elif text == '7':
        send_message('students', student_manager, topic)
        print(message)
    elif text == '8':
        show_super_admin_menu()
    else:
        print("Invalid input, enter an option again!")
        send_message_to_all()


def show_super_admin_menu():
    """
    This function displays the super admin menu with options to create an admin, verify admins, send a message, or go back.
    """
    while True:
        text = input("""
    1. Create admin.
    2. Verify admins. 
    3. Send message to all.
    4. Go to back.

    Choose an option above: """).strip()

        if text == '1':
            if create_admin():
                print("Admin created, please ask them to verify their email")
        elif text == '2':
            verify_admins()
        elif text == '3':
            send_message_to_all()
        elif text == '4':
            show_auth_menu()
        else:
            print("Invalid input, try again")


def show_auth_menu():
    """
    This function displays the authentication menu with options to log in or exit.
    """
    text = """
1. Log in.
2. Exit.
"""
    print(text)

    user_input = input("Choose an option above: ").strip()

    if user_input == "1":
        login = input("Enter a login: ").strip()
        password = input("Enter a password: ").strip()
        if check_super_admin(login=login, password=password):
            show_super_admin_menu()
        elif check_admin(login=login, password=password):
            show_admin_menu()
        elif check_student(login=login, password=password):
            show_student_menu()
        elif check_teacher(login=login, password=password):
            show_teacher_menu()
        else:
            print("System cannot detect you, please try later")
            show_auth_menu()
    elif user_input == "2":
        print("You quit the program!")
        return
    else:
        print("Invalid input, try again")
        show_auth_menu()


if __name__ == '__main__':
    show_auth_menu()
