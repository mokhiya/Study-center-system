from file_manager import teacher_manager

teacher_data = teacher_manager.read_data()


def check_teacher(login, password):
    try:
        for teacher in teacher_data:
            if teacher and login == teacher.get('login') and password == teacher.get('password'):
                teacher['status'] = True
                return True
    except Exception as e:
        print(f"An error occurred while reading teacher data: {e}")
    return False


def get_logged_in_teacher():
    for teacher in teacher_data:
        if teacher['status']:
            return teacher
    return None


def change_password():

    original_password = input("What password is used in registration? ").strip()
    changed_password = input("What would you like to change the password to? ").strip()

    for data in teacher_data:
        if data["password"] == original_password:
            data["password"] = changed_password
            print("Password changed successfully.")
            break
    else:
        print("Password not found.")


logged_in_teacher = get_logged_in_teacher()


def show_groups():
    if logged_in_teacher:
        print(f"\nGroups for {logged_in_teacher['full_name']}:\n")
        if 'groups' in logged_in_teacher and logged_in_teacher['groups']:
            for group in logged_in_teacher['groups']:
                print(f"Group Name: {group['name']}, Subject: {group['subject']}, Room: {group['room']}")
        else:
            print("You are not given any groups.")
    else:
        print("No student is logged in.")


def show_classes():
    if logged_in_teacher:
        print(f"\nClasses for {logged_in_teacher['full_name']}:\n")
        if 'groups' in logged_in_teacher and logged_in_teacher['groups']:
            for group in logged_in_teacher['groups']:
                print(f"Class Name: {group['subject']}, Weekdays: {group['weekdays']}, Time: {group['time']}")
        else:
            print("You have no scheduled classes.")
    else:
        print("No student is logged in.")


def start_end_lesson():
    show_classes()
    class_choice = input("\nEnter lesson name: ").title().strip()
    start_end_lesson = input("Would you like to 1.start or 2.end lesson? ").strip()

    if start_end_lesson == "1":



def show_teacher_menu():
    while True:
        text = input("""
        1. Change my password.
        2. My groups.
        3. My classes.
        4. Log out.

        Choose an option above: """)

        if text == '1':
            change_password()
        elif text == '2':
            show_groups()
        elif text == '3':
            pass
        elif text == '4':
            print("Logging out.")
            # Set the student's status to False
            for teacher in teacher_data:
                if teacher.get('status'):
                    teacher['status'] = False
            teacher_manager.write_data(teacher_data)
            break
        else:
            print('Invalid option, try again')
