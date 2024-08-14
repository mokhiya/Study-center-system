class Student:
    """
    This function initializes a Student object with the provided login, password,
    full name, gender, and email. It also sets the default status to False and
    initializes an empty list for groups.

    Args:
        login (str): The login username for the student.
        password (str): The password for the student's account.
        full_name (str): The full name of the student.
        gender (str): The gender of the student.
        email (str): The email address of the student.
    """
    def __init__(self, login, password, full_name, gender, email):
        self.login = login
        self.password = password
        self.full_name = full_name
        self.email = email
        self.gender = gender
        self.status = False
        self.groups = []
