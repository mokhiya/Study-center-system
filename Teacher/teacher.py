class Teacher:
    def __init__(self, login, password, full_name, gender, email):
        """
        This constructor initializes a Teacher object with the following attributes:

        - `login`: A string representing the login name for the teacher.
        - `password`: A string representing the password for the teacher.
        - `full_name`: A string representing the full name of the teacher.
        - `gender`: A string representing the gender of the teacher.
        - `email`: A string representing the email address of the teacher.
        - `status`: A boolean indicating whether the teacher is logged in (defaults to False).
        - `groups`: A list to store groups that the teacher is associated with (initialized as an empty list).
        """
        self.login = login
        self.password = password
        self.full_name = full_name
        self.gender = gender
        self.email = email
        self.status = False
        self.groups = []
