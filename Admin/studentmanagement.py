from Student.student import Student
from file_manager import student_manager


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


