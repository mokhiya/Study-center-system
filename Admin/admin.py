from file_manager import admin_manager
from Admin.teachermanagement import create_teacher, delete_teacher
from Admin.groupmanagement import create_group


def teacher_management():
    text = input("""
    1. Create a new teacher.
    2. See all teachers.
    3. Add teacher to groups.
    4. Add lessons to teachers.
    5. Remove teacher from groups.
    6. Remove lessons from teachers.
    7. Delete teacher account.
    8. Go to back.
    
    Choose an option above
    """)

    if text == "1":
        if create_teacher():
            print("Teacher account created successfully.")
            return teacher_management()
    elif text == "2":
        pass
    elif text == "3":
        pass
    elif text == "4":
        pass
    elif text == "5":
        pass
    elif text == "6":
        delete_teacher()
    else:
        return False

def student_management():
    text = input("""
        1. Create a new student.
        2. See all students.
        3. Add student to groups.
        4. Remove student from groups.
        5. Delete student account.
        6. Go to back. 

        Choose an option above
        """)

    if text == "1":
        pass
    elif text == "2":
        pass
    elif text == "3":
        pass
    elif text == "4":
        pass
    else:
        return False


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

