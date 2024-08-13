from Teacher.teacher import Teacher
from file_manager import teacher_manager, group_manager


def create_teacher():
    teacher_login = input("Create teacher's login: ").strip()
    teacher_password = input("Create teacher's password: ").strip()
    teacher_name = input("Enter teacher's full name: ").title().strip()
    teacher_email = input("Enter teacher's email: ").strip()

    teacher = Teacher(teacher_login, teacher_password, teacher_name, teacher_email)
    teacher_manager.add_data(teacher.__dict__)
    return True


def show_all_teachers():
    teacher_data = teacher_manager.read_data()

    if not teacher_data:  # If teacher_data is empty
        print("{:<30} {:<30}".format("No Teachers found", ''))
        return False

    print("Teachers:\n")
    print("{:<30} {:<30}".format("Full name", "Email"))
    print("-" * 50)

    for data in teacher_data:
        if data:  # Checking if data is not empty
            print("{:<30} {:<30}".format(data['full_name'], data['email']))

    return True


def add_teacher_to_groups():
    groups = group_manager.read_data()
    if not groups:  # If no group is created yet
        print("{:<30} {:<30}".format("No groups created yet, please, first create groups", ''))
        return False

    show_all_teachers()

    print("\n\nAvailable groups:\n")
    print("{:<30} {:<30} {:<15} {:<10}".format("Group name", "Subject", "Start date", "Duration"))
    print("-" * 50)

    for data in groups:
        if data:
            print("{:<30} {:<30} {:<15} {:<10}".format(data['name'], data['subject'], data['start'], data['duration']))

    teacher_name = input("\nEnter teacher's full name: ").title().strip()
    group_name = input("Enter group name to add to teacher: ").title().strip()

    # Find the teacher in the list
    teacher_data = teacher_manager.read_data()
    selected_teacher = next((teacher for teacher in teacher_data if teacher['full_name'] == teacher_name), None)

    if not selected_teacher:
        print("No such teacher found:", teacher_name)
        return add_teacher_to_groups()

    # Find the group in the list
    selected_group = next((group for group in groups if group['name'] == group_name), None)

    if not selected_group:
        print("No such group found:", group_name)
        return add_teacher_to_groups()

    # Add the selected group to the teacher's 'groups' list
    selected_teacher.setdefault('groups', []).append(selected_group)

    # Update the teachers data
    teacher_manager.write_data(teacher_data)

    print(f"Group {group_name} added to teacher {teacher_name}'s groups list successfully.")
    return True



def delete_teacher():
    teacher_login = input("Enter teacher's login to delete account: ").strip()
    teacher_data = teacher_manager.read_data()
    for teacher in teacher_data:
        if teacher['login'] == teacher_login:
            teacher_manager.delete_data(teacher)
            return True
        return False
