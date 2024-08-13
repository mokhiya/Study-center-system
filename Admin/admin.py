from file_manager import admin_manager

"""
2. Student management.
3. Group management.
4. Payment management.
5. Logout.

Choose an option above: """


def teacher_management():
    text = input("""
    1. Create a new teacher.
    2. Add teacher to groups.
    3. Add lessons to teachers.
    4. Remove teacher from groups.
    5. Remove lessons from teachers.
    6. Delete teacher account.
    7. Go to back.
    
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
    elif text == "5":
        pass
    elif text == "6":
        pass
    else:
        return False

def student_management():
    text = input("""
        1. Create a new student.
        2. Add student to groups.
        3. Remove student from groups.
        4. Delete student account.
        5. Go to back. 

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
        pass
    elif text == "2":
        pass
    elif text == "3":
        pass
    else:
        return False

