import smtplib
import random
import threading
from email.message import EmailMessage
from file_manager import admin_manager

super_admin_login = "admin"
super_admin_password = "0000"


class Admin:
    """
    Class representing an admin user.

    Attributes:
    - login: Admin's login name.
    - password: Admin's password.
    - email: Admin's email address.
    - verified: Verification status of the admin account.
    """

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email
        self.verified = False


def create_admin():
    """
    This function creates a new admin account, validates the email, and sends a verification email.
    """
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

    threading.Thread(target=send_verification_email, args=(admin_email,)).start()


def send_email(smtp_server, smtp_port, smtp_sender, smtp_password, recipient_email, subject, message):
    """
    This function sends an email to a recipient using the specified SMTP server and credentials.

    Parameters:
    - smtp_server: The SMTP server address.
    - smtp_port: The SMTP server port.
    - smtp_sender: The sender's email address.
    - smtp_password: The sender's email password.
    - recipient_email: The recipient's email address.
    - subject: The subject of the email.
    - message: The body of the email.
    """
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_sender, smtp_password)
            msg = EmailMessage()
            msg.set_content(message)
            msg['Subject'] = subject
            msg['From'] = smtp_sender
            msg['To'] = recipient_email
            server.send_message(msg)
            print(f"Message sent to {recipient_email}!")
    except smtplib.SMTPException as e:
        print(f"Error: unable to send email to {recipient_email}. Error: {e}")


# SMTP server configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_sender = 'mohiyaxonuzokova@gmail.com'
smtp_password = 'svjd fcgt yhsg qjuk'


def send_message(type_p, file_manager, topic):
    """
    This function sends a notification message to all entities of a specified type (admins, teachers, or students).

    Parameters:
    - type_p: The type of entities to notify ('admins', 'teachers', or 'students').
    - file_manager: The file manager to read data from.
    - topic: The notification topic.
    """
    data = file_manager.read_data()
    subject = f"Important Notification: {topic}"

    threads = []

    for item in data:
        if type_p in item and 'email' in item:
            recipient_email = item['email']
            message = f"Subject: {subject}\n\n{topic}"

            thread = threading.Thread(
                target=send_email,
                args=(smtp_server, smtp_port, smtp_sender,
                      smtp_password, recipient_email, subject, message)
            )
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()


def send_verification_email(email):
    """
    This function sends a verification email with a code to the specified email address.

    Parameters:
    - email: The email address to send the verification code to.
    """
    verification_code = str(random.randint(100000, 999999))
    subject = "Email Verification"
    message = f"Your verification code is {verification_code}"

    email_content = f"Subject: {subject}\n\n{message}"

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_sender, smtp_password)
        msg = EmailMessage()
        msg.set_content(message)
        msg['Subject'] = subject
        msg['From'] = smtp_sender
        msg['To'] = email
        server.send_message(msg)
        server.quit()
        print(f"Verification code sent to {email}!")
    except smtplib.SMTPException as e:
        print(f"Error: unable to send email to {email}. Error: {e}")

    admins = admin_manager.read_data()
    for admin in admins:
        if admin.get('email') == email:
            admin['verification_code'] = verification_code
            admin_manager.write_data(admins)
            break


def verify_admins():
    """
    This function verifies an admin account by checking the provided email and verification code.
    """
    admins = admin_manager.read_data()

    unverified_admins = [
        admin for admin in admins
        if 'email' in admin and not admin.get('verified', False)
    ]

    if not unverified_admins:
        print("No unverified admins found.")
        return False

    print("Unverified admins:")
    for admin in unverified_admins:
        print(f"Email: {admin['email']}")

    email_to_verify = input("Enter the email of the admin you want to verify: ").strip()
    selected_admin = next((admin for admin in unverified_admins if admin['email'] == email_to_verify), None)

    if not selected_admin:
        print("No admin found with the provided email.")
        return False

    while True:
        entered_code = input(f"Enter the verification code sent to {selected_admin['email']}: ")

        if entered_code == selected_admin.get('verification_code'):
            print("Verification successful!")
            selected_admin['verified'] = True
            selected_admin.pop('verification_code', None)
            admin_manager.write_data(admins)
            return True
        else:
            print("Verification failed. The code was incorrect. Please try again.")


def check_super_admin(login, password):
    """
    This function checks if the provided login and password match the super admin credentials.

    Parameters:
    - login: The login name.
    - password: The password.

    Returns:
    - True if the credentials match the super admin credentials, False otherwise.
    """
    return login == super_admin_login and password == super_admin_password


def check_admin(login, password):
    """
    This function checks if the provided login and password match an existing admin's credentials.

    Parameters:
    - login: The login name.
    - password: The password.

    Returns:
    - True if the credentials match an existing admin's credentials and the account is verified, False otherwise.
    """
    try:
        admins = admin_manager.read_data()
        for admin in admins:
            if login == admin.get('login') and password == admin.get('password'):
                if admin['verified']:
                    return True
                else:
                    print("Your account is not verified. Please check your email for verification instructions.")
                    return False
    except Exception as e:
        print(f"An error occurred while reading admin data: {e}")
    return False
