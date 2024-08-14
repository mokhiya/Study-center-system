from file_manager import teacher_manager, group_manager

teacher_data = teacher_manager.read_data()
group_data = group_manager.read_data()


def check_teacher(login, password):
    """
    This function checks if the provided login and password match any teacher in the teacher data.

    Parameters:
    - login (str): The teacher's login name.
    - password (str): The teacher's password.

    Returns:
    - bool: True if the login is successful, False otherwise.
    """
    try:
        for teacher in teacher_data:
            if teacher and login == teacher.get('login') and password == teacher.get('password'):
                teacher['status'] = True
                teacher_manager.write_data(teacher)
                return True
    except Exception as e:
        print(f"An error occurred while reading teacher data: {e}")
    return False


def get_logged_in_teacher():
    """
    This function returns the currently logged-in teacher by checking the status of each teacher
    in the teacher data.

    Returns:
    - dict: The logged-in teacher's data if found, None otherwise.
    """
    for teacher in teacher_data:
        if isinstance(teacher, dict) and teacher.get('status'):
            return teacher
    return None


def change_password():
    """
    This function allows a logged-in teacher to change their password.
    """
    original_password = input("What password is used in registration? ").strip()
    changed_password = input("What would you like to change the password to? ").strip()

    for data in teacher_data:
        if data["password"] == original_password:
            data["password"] = changed_password
            teacher_manager.write_data(data)
            print("Password changed successfully.")
            break
    else:
        print("Password not found.")
        return change_password()


logged_in_teacher = get_logged_in_teacher()


def show_groups():
    """
    This function displays the groups associated with the logged-in teacher.
    """
    if not logged_in_teacher:
        print("No teacher is logged in.")
        return

    print(f"\nGroups for {logged_in_teacher['full_name']}:")
    print("------------------------------------------")

    if logged_in_teacher.get('groups'):
        for group in logged_in_teacher['groups']:
            print(f"Group name: {group['name']} | Subject: {group['subject']} | Room: {group['room']}")
    else:
        print("You are not assigned to any groups.")


def show_classes():
    """
    This function displays the classes (groups) associated with the logged-in teacher.
    """
    if logged_in_teacher:
        print(f"\nClasses for {logged_in_teacher['full_name']} teacher:\n")
        if 'groups' in logged_in_teacher and logged_in_teacher['groups']:
            for group in logged_in_teacher['groups']:
                print(f"Class Name: {group['subject']} | Weekdays: {group['weekdays']} | Time: {group['time']}")
        else:
            print("You have no scheduled classes.")
    else:
        print("No classes found.")


def start_or_end_lesson():
    """
    This function allows the logged-in teacher to start or end a lesson (class).
    """
    show_classes()  # This function should display all available classes/groups
    class_choice = input("\nEnter lesson name: ").title().strip()
    start_end_lesson = input("Would you like to 1. start or 2. end the lesson? ").strip()

    selected_group = next((group for group in group_data if group['subject'].title() == class_choice), None)

    if not selected_group:
        print("No matching lesson found.")
        return start_or_end_lesson()

    if start_end_lesson == "1":
        selected_group['status'] = True
        print(f"Lesson '{selected_group['subject']}' started.")
        show_groups()
    elif start_end_lesson == "2":
        selected_group['status'] = False
        print(f"Lesson '{selected_group['subject']}' ended.")
    else:
        print("Invalid choice.")
        return start_or_end_lesson()

    group_manager.write_data(group_data)
    show_teacher_menu()


def show_teacher_menu():
    """
    This function displays the menu for a logged-in teacher, providing options to change the password,
    view groups, view classes, start or end a lesson, or log out.
    """
    while True:
        text = input("""
        1. Change my password.
        2. My groups.
        3. My classes.
        4. Start or end lesson.
        5. Log out.

        Choose an option above: """)

        if text == '1':
            change_password()
        elif text == '2':
            show_groups()
        elif text == '3':
            show_classes()
        elif text == '4':
            start_or_end_lesson()
        elif text == '5':
            print("Logging out.")
            for teacher in teacher_data:
                if teacher.get('status'):
                    teacher['status'] = False
            teacher_manager.write_data(teacher_data)
            break
        else:
            print('Invalid option, try again')
