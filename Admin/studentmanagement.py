from Student.student import Student
from file_manager import student_manager, group_manager


def create_new_student():
    student_login = input("Create student login: ").strip()
    student_password = input("Create student password: ").strip()
    student_full_name = input("Enter student full name: ").title().strip()
    student_gender = input("Enter student gender: ").title().strip()
    while True:  # Validating email format
        student_email = input("Enter student email: ").strip()
        if student_email.endswith('@gmail.com'):
            break
        else:
            print("Invalid input, enter an email again!")

    student = Student(login=student_login, password=student_password,
                      full_name=student_full_name, email=student_email, gender=student_gender)

    print("Student account created successfully!")
    student_manager.add_data(student.__dict__)


def show_all_students():
    student_data = student_manager.read_data()

    if not student_data:  # If student_data is empty
        print("{:<30} {:<30}".format("No students found", ''))
        return False

    print("Students:\n")
    print("{:<30} {:<30}".format("Full name", "Email", "Group"))
    print("-" * 80)

    for data in student_data:
        if data:  # Checking if data is not empty
            print("{:<30} {:<30}".format(data['full_name'], data['email'], data['groups']))

    return True
