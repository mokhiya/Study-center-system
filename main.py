super_admin_login = "admin"
super_admin_password = "0000"


def show_super_admin_menu():
    while True:
        text = input("""
    1. Create admin.
    2. Quit the program.

    Choose an option above: """).strip()

        if text == '1':
            pass
        elif text == '2':
            pass
        else:
            print("Invalid input, try again")


def check_super_admin(login, password):
    if login == super_admin_login and password == super_admin_password:
        return True
    return False


def show_auth_menu():
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
        else:
            print("System cannot detect you, please try later")
            show_auth_menu()
    elif user_input == "2":
        print("You quit the program!")
        return
    else:
        print("Invalid input, try again")
        show_auth_menu()


#
# def check_teacher(login, password):
#     all_teachers = teacher_manager.read()
#     for teacher in all_teachers:
#         if teacher['login'] == login and teacher['password'] == password:
#             return True
#     return False
#
#
# def check_student(login, password):
#     all_students = student_manager.read()
#     for student in all_students:
#         if student['login'] == login and student['password'] == password:
#             return student
#     return None

#
# def show_teacher_menu():
#     print("Teacher Login")
#     login = input("Enter your login: ").strip()
#     password = input("Enter your password: ").strip()
#
#     if check_teacher(login, password):
#         while True:
#             print("""
# 1. Show my active lessons
# 2. Start lesson
# 3. Show my ended lessons
# 4. Logout
# """)
#             choice = input("Choose an option: ").strip()
#
#             if choice == '1':
#                 show_active_lessons_teacher(login)
#             elif choice == '2':
#                 start_lesson(login)
#             elif choice == '3':
#                 pass
#             elif choice == '4':
#                 break
#             else:
#                 print("Invalid option. Please try again.")
#     else:
#         print("Invalid login or password.")
#
#
# def show_student_menu():
#     print("Student Login")
#     login = input("Enter your login: ").strip()
#     password = input("Enter your password: ").strip()
#
#     student = check_student(login, password)
#     if student:
#         while True:
#             print("""
# 1. Show my active lessons
# 2. Show my grade
# 3. Show my grade by subject
# 4. Logout
# """)
#             choice = input("Choose an option: ").strip()
#
#             if choice == '1':
#                 show_active_lessons_student(student)
#             elif choice == '2':
#                 show_my_grade(student)
#             elif choice == '3':
#                 show_grade_by_subject(student)
#             elif choice == '4':
#                 break
#             else:
#                 print("Invalid option. Please try again.")
#     else:
#         print("Invalid login or password.")
#
#
# def show_management(topic):
#     user_input = input(f"""
# What would you like to do?
# 1. Create a {topic}.
# 2. Read all data about {topic}.
# 3. Update all data about {topic}.
# 4. Delete {topic}
# 5. Go to back.
# Choose an option above: """).strip()
#
#     if user_input == '1':
#         if topic == "teacher":
#             if create_teacher():
#                 print("Congrats!")
#             else:
#                 print("Failed to create teacher")
#             show_management(topic="teacher")
#         elif topic == "subject":
#             create_subject()
#             show_management(topic="subject")
#         elif topic == "group":
#             create_group()
#             show_management(topic="group")
#         elif topic == "student":
#             create_student()
#             show_management(topic="student")
#         elif topic == "lesson":
#             create_lesson()
#             show_management(topic="lesson")
#     elif user_input == '2':
#         if topic == "teacher":
#             print(f"All data about {topic}")
#             read_teachers()
#             show_management(topic="teacher")
#         elif topic == "subject":
#             read_subjects()
#             show_management(topic="subject")
#         elif topic == "group":
#             read_groups()
#             show_management(topic="group")
#         elif topic == "student":
#             read_students()
#             show_management(topic="student")
#         elif topic == "lesson":
#             read_lessons()
#             show_management(topic="lesson")
#     elif user_input == '3':
#         if topic == "teacher":
#             print(f"Updating all data about {topic}!")
#             if update_teacher():
#                 print("Teacher's classes updated successfully!")
#             else:
#                 print("Teacher not found or update failed.")
#             show_management(topic="teacher")
#         elif topic == "subject":
#             update_subject()
#             show_management(topic="subject")
#         elif topic == "group":
#             update_group()
#             show_management(topic="group")
#         elif topic == "student":
#             update_student()
#             show_management(topic="student")
#         elif topic == "lesson":
#             update_lesson()
#             show_management(topic="lesson")
#     elif user_input == '4':
#         print(f"Deleting {topic}!")
#         if topic == "teacher":
#             if delete_teacher():
#                 pass
#             print("Teacher's data could not be deleted, try again later")
#             show_management(topic="teacher")
#         elif topic == "subject":
#             delete_subject()
#             show_management(topic="subject")
#         elif topic == "group":
#             delete_group()
#             show_management(topic="group")
#         elif topic == "student":
#             delete_student()
#             show_management(topic="student")
#         elif topic == "lesson":
#             delete_lesson()
#             show_management(topic="lesson")
#     elif user_input == '5':
#         show_admin_menu()
#     else:
#         print("Invalid input, try again")
#         show_admin_menu()
#
#
# def show_admin_menu():
#     while True:
#         text = input("""
# 1. Subject management.
# 2. Teacher management.
# 3. Group management.
# 4. Student management.
# 5. Manage lessons.
# 6. Show all lessons.
# 7. Log out.
# Choose an option above: """).strip()
#
#         if text == '1':
#             show_management(topic="subject")
#         elif text == '2':
#             show_management(topic="teacher")
#         elif text == '3':
#             show_management(topic="group")
#         elif text == '4':
#             show_management(topic="student")
#         elif text == '5':
#             show_management(topic="lesson")
#         elif text == '6':
#             pass
#         elif text == '7':
#             show_auth_menu()
#         else:
#             print("Invalid input, try again")
#


if __name__ == '__main__':
    show_auth_menu()
