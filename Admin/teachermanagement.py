from Teacher.teacher import Teacher
from file_manager import teacher_manager


def create_teacher():
    teacher_login = input("Create teacher's login: ").strip()
    teacher_password = input("Create teacher's password: ").strip()
    teacher_name = input("Enter teacher's full name: ").strip()
    teacher_email = input("Enter teacher's email: ").strip()

    teacher = Teacher(teacher_login, teacher_password, teacher_name, teacher_email)
    teacher_manager.add_data(teacher.__dict__)
    return True


def delete_teacher():
    teacher_login = input("Enter teacher's login to delete account: ").strip()
    teacher_data = teacher_manager.read_data()
    for teacher in teacher_data:
        if teacher['login'] == teacher_login:
            teacher_manager.delete_data(teacher)
            return True
        return False
