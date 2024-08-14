import smtplib
import random
from file_manager import admin_manager

super_admin_login = "admin"
super_admin_password = "0000"


class Admin:
    def __init__(self, login, password, email, verified=False):
        self.login = login
        self.password = password
        self.email = email
        self.verified = verified


def create_admin():
    admin_login = input("Enter admin's login name: ")
    admin_password = input("Enter admin's password: ")

    while True:  # Validating email format
        admin_email = input("Enter admin's email: ").strip()
        if admin_email.endswith('@gmail.com'):
            break
        else:
            print("Invalid input, enter an email again!")

    admin = Admin(login=admin_login, password=admin_password, email=admin_email)
    admin_manager.add_data(admin.__dict__)


def send_verification_email(email, verification_code):
    stmp_server = 'smtp.gmail.com'
    stmp_port = 587
    stmp_sender = 'your_email@gmail.com'
    stmp_password = 'your_generated_app_password_here'

    subject = "Email Verification"
    message = f"Your verification code is {verification_code}"

    email_content = f"Subject: {subject}\n\n{message}"

    try:
        server = smtplib.SMTP(stmp_server, stmp_port)
        server.starttls()
        server.login(stmp_sender, stmp_password)
        server.sendmail(stmp_sender, email, email_content)
        server.quit()
        print(f"Verification code sent to {email}!")
    except smtplib.SMTPException as e:
        print(f"Error: unable to send email to {email}. Error: {e}")


def verify_admins():
    admins = admin_manager.read_data()

    for admin in admins:
        if 'email' in admin and not admin.get('verified', False):
            verification_code = str(random.randint(100000, 999999))  # Generate a 6-digit random code
            send_verification_email(admin['email'], verification_code)

            entered_code = input(f"Enter the verification code sent to {admin['email']}: ")

            if entered_code == verification_code:
                print("Verification successful!")
                admin['verified'] = True
            else:
                print("Verification failed. The code was incorrect.")

    admin_manager.write_data(admins)
    return True


def send_message_to_all_admins():
    admins = admin_manager.read_data()
    for admin in admins:
        if 'email' in admin and not admin.get('verified', False):
            pass


def check_super_admin(login, password):
    if login == super_admin_login and password == super_admin_password:
        return True
    return False


def check_admin(login, password):
    try:
        admin = admin_manager.read_data()
        for admin in admin:
            if admin and login == admin.get('login') and password == admin.get('password'):
                return True
    except Exception as e:
        print(f"An error occurred while reading admin data: {e}")
    return False
