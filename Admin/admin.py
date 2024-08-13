from file_manager import admin_manager, student_manager, teacher_manager
from Admin.teachermanagement import (create_teacher, show_all_teachers, add_entity_to_groups,
                                     remove_entity_from_groups, delete_teacher)
from Admin.studentmanagement import create_new_student, show_all_students
from Admin.groupmanagement import create_group



def teacher_management():
    text = input("""
    1. Create a new teacher.
    2. See all teachers.
    3. Add teacher to groups.
    4. Remove teacher from groups.
    5. Delete teacher account.
    6. Go to back.
    
    Choose an option above
    """)

    if text == "1":
        if create_teacher():
            print("Teacher account created successfully.")
            return teacher_management()
    elif text == "2":
        show_all_teachers()
        return teacher_management()
    elif text == "3":
        add_entity_to_groups('teacher')
        return teacher_management()
    elif text == "4":
        remove_entity_from_groups("teacher", "full_name", "teachers", teacher_manager)
        return teacher_management()
    elif text == "5":
        delete_teacher()
        return teacher_management()
    elif text == "6":
        return show_admin_menu()
    else:
        print("---------------------")
        print("Invalid option!")
        print("---------------------\n")
        return teacher_management()


def student_management():
    text = input("""
        1. Create a new student.
        2. Add student to groups.
        3. Remove student from groups.
        4. Delete student account.
        5. See all students.
        6. Go to back. 

        Choose an option above
        """)

    if text == "1":
        create_new_student()
        return student_management()
    elif text == "2":
        add_entity_to_groups('student')
        return student_management()
    elif text == "3":
        remove_entity_from_groups("student", "full_name", "students", student_manager)
        return student_management()
    elif text == "4":
        pass
    elif text == "5":
        show_all_students()
        return student_management()
    else:
        return show_admin_menu()


def group_management():
    text = input("""
        1. Create a new group.
        2. See all groups.
        3. Delete group.
        4. Go to back. 

        Choose an option above
        """)

    if text == "1":
        create_group()
        return group_management()
    elif text == "2":
        pass
    elif text == "3":
        pass
    else:
        return False


def show_admin_menu():
    while True:
        text = input("""
        1. Teacher management.
        2. Student management.
        3. Group management.
        4. Payment management.
        5. Logout.

        Choose an option above: """).strip()

        if text == '1':
            if teacher_management():
                show_admin_menu()
        elif text == '2':
            if student_management():
                show_admin_menu()
        elif text == '3':
            if group_management():
                show_admin_menu()
        elif text == '4':
            pass
        else:
            print("Invalid input, try again")
