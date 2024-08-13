class Student:
    def __init__(self, login, password, full_name, gender, email):
        self.login = login
        self.password = password
        self.full_name = full_name
        self.email = email
        self.gender = gender
        self.status = False
        self.groups = []
        self.lessons = []