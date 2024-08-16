from file_manager import student_manager


def check_student(login, password):
    """
    This function checks if a student with the provided login and password exists
    in the student data.

    Args:
        login (str): The login username for the student.
        password (str): The password for the student's account.

    Returns:
        bool: True if the student is found and authenticated, False otherwise.
    """
    # Loads the student data from the file
    student_data = student_manager.read_data()

    try:
        for student in student_data:
            if student and login == student.get('login') and password == student.get('password'):
                student['status'] = True
                return True
    except Exception as e:
        print(f"An error occurred while reading student data: {e}")
    return False


def get_logged_in_student():
    """
    This function retrieves the currently logged-in student based on their status.

    Returns:
        dict: The data of the logged-in student, or None if no student is logged in.
    """
    # Loads the student data from the file
    student_data = student_manager.read_data()

    for student in student_data:
        if student['status']:
            return student
    return None


def change_personal_data():
    """
    This function allows the logged-in student to change their personal data including full name, password, or email.

    Returns:
        None
    """
    student_input = input("What would you like to change?\n "
                          "1. Full name.\n"
                          "2. Password.\n"
                          "3. Email.\n"
                          "Enter the number corresponding to your choice: ").strip()
    # Loads the student data from the file
    student_data = student_manager.read_data()

    if student_input == "1":
        original_name = input("What name is used in registration? ").title().strip()
        changed_name = input("What would you like to change the name to? ").title().strip()
        for data in student_data:
            if data['full_name'] == original_name:
                data['full_name'] = changed_name
                print("Name changed successfully.")
                break
        else:
            print("Name not found.")

    elif student_input == "2":
        original_password = input("What password is used in registration? ").strip()
        changed_password = input("What would you like to change the password to? ").strip()

        for data in student_data:
            if data["password"] == original_password:
                data["password"] = changed_password
                print("Password changed successfully.")
                break
        else:
            print("Password not found.")

    elif student_input == "3":
        original_email = input("What email is used in registration? ").strip()
        changed_email = input("What would you like to change the email to? ").strip()

        for data in student_data:
            if data["email"] == original_email:
                data["email"] = changed_email
                print("Email changed successfully.")
                break
        else:
            print("Email not found.")

    else:
        print("Invalid input. Please try again.")
        change_personal_data()

    # Write the updated student_data back to the file
    student_manager.write_data(student_data)


def show_my_groups():
    """
    This function displays all the groups that the logged-in student is currently enrolled in.
    If no student is logged in, or if the student is not enrolled in any groups, it displays appropriate messages.

    Returns:
        None
    """
    logged_in_student = get_logged_in_student()

    if logged_in_student:
        print(f"\nGroups for {logged_in_student['full_name']}:\n")
        if 'groups' in logged_in_student and logged_in_student['groups']:
            for group in logged_in_student['groups']:
                print(f"Group Name: {group['name']}, Subject: {group['subject']}, Room: {group['room']}")
        else:
            print("You are not enrolled in any groups.")
    else:
        print("No student is logged in.")


def show_my_classes():
    """
    This function displays all the classes that the logged-in student is currently scheduled for.

    Returns:
        None
    """
    logged_in_student = get_logged_in_student()

    if logged_in_student:
        print(f"\nClasses for {logged_in_student['full_name']}:\n")
        if 'groups' in logged_in_student and logged_in_student['groups']:
            for group in logged_in_student['groups']:
                print(f"Class Name: {group['subject']}, Weekdays: {group['weekdays']}, Time: {group['time']}")
        else:
            print("You have no scheduled classes.")
    else:
        print("No student is logged in.")


def show_student_menu():
    """
    This function displays a menu for the logged-in student with options to change their data,
    view their groups, view their classes, or log out. It loops until the student chooses to log out.

    The available options are:
        1. Change my data - Calls the `change_personal_data` function.
        2. My groups - Calls the `show_my_groups` function.
        3. My classes - Calls the `show_my_classes` function.
        4. Log out - Logs the student out by setting their status to False and exits the menu.

    Returns:
        None
    """
    while True:
        text = input("""
        1. Change my data.
        2. My groups.
        3. My classes.
        4. Log out.

        Choose an option above: """)

        if text == '1':
            change_personal_data()
        elif text == '2':
            show_my_groups()
        elif text == '3':
            show_my_classes()
        elif text == '4':
            print("Logging out.")
            # Loads the student data from the file
            student_data = student_manager.read_data()
            # Set the student's status to False
            for student in student_data:
                if student.get('status'):
                    student['status'] = False
            student_manager.write_data(student_data)
            break
        else:
            print('Invalid option, try again')
