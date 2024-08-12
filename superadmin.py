from file_manager import admin_manager

class Admin:
    def __init__(self, login, password):
        self.login = login
        self.password = password


def create_admin():
    admin_login = input("Enter admin's login name: ")
    admin_password = input("Enter admin's password: ")

    while True:  # Validating email format
        admin_email = input("Enter admin's email: ").strip()
        if admin_email.endswith('@gmail.com'):
            break
        else:
            print("Invalid input, enter an email again!")

    admin_data = {
        'admin_login': admin_login,
        'admin_password': admin_password,
        'admin_email': admin_email
    }
    admin_manager.add_data(admin_data)