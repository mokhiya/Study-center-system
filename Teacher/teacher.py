from file_manager import teacher_manager

class Teacher:
    def __init__(self, login, password, full_name, gender, email):
        self.login = login
        self.password = password
        self.full_name = full_name
        self.gender = gender
        self.email = email
        self.status = False
        self.groups = []
        self.lessons = []


