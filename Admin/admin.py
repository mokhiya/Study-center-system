"""
This module handles the administrative functionalities for managing teachers, students, and groups in the system.
It provides interactive menus for creating, viewing, updating, and deleting entities,
and for navigating between different management areas.
"""

from file_manager import student_manager, teacher_manager
from Admin.teachermanagement import (create_teacher, show_all_teachers, add_entity_to_groups,
                                     remove_entity_from_groups, delete_teacher)
from Admin.studentmanagement import create_new_student, show_all_students, delete_student
from Admin.groupmanagement import create_group, show_all_groups, delete_group


def teacher_management():
    """
    This function manages teacher-related operations through an interactive menu.
    """
    text = input("""
    1. Create a new teacher.
    2. See all teachers.
    3. Add teacher to groups.
    4. Remove teacher from groups.
    5. Delete teacher account.
    6. Go to back.
    
    Choose an option above: """)

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
    """
    This function manages student-related operations through an interactive menu.
    """
    text = input("""
        1. Create a new student.
        2. Add student to groups.
        3. Remove student from groups.
        4. Delete student account.
        5. See all students.
        6. Go to back. 

        Choose an option above: """)

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
        delete_student()
        return student_management()
    elif text == "5":
        show_all_students()
        return student_management()
    else:
        return show_admin_menu()


def group_management():
    """
    This function manages group-related operations through an interactive menu.
    """
    text = input("""
        1. Create a new group.
        2. See all groups.
        3. Delete group.
        4. Go to back. 

        Choose an option above: """)

    if text == "1":
        create_group()
        return group_management()
    elif text == "2":
        show_all_groups()
        return group_management()
    elif text == "3":
        if delete_group():
            pass
        return group_management()
    else:
        return show_admin_menu()


def show_admin_menu():
    """
    This function displays the main admin menu and handles navigation to different management areas.
    """
    while True:
        text = input("""
        1. Teacher management.
        2. Student management.
        3. Group management.
        4. Quit.

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
            print("Quitting..."
                  "Start the program again to log in")
            return
        else:
            print("Invalid input, try again")
