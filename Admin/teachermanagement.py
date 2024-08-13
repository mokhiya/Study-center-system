from Teacher.teacher import Teacher
from file_manager import teacher_manager

def create_teacher():
    teacher_login = input("Create teacher's login: ").strip()
    teacher_password = input("Create teacher's password: ").strip()
    teacher_name = input("Enter teacher's full name: ").strip()
    teacher_email = input("Enter teacher's email: ").strip()

    teacher = Teacher(teacher_login, teacher_password, teacher_name, teacher_email)
    teacher_manager.add_data(teacher.__dict__)


