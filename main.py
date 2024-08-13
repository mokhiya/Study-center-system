from file_manager import admin_manager
from superadmin import create_admin, check_super_admin, check_admin


super_admin_login = "admin"
super_admin_password = "0000"


def show_super_admin_menu():
    while True:
        text = input("""
    1. Create admin.
    2. Send message to all admins.
    3. Go to back.

    Choose an option above: """).strip()

        if text == '1':
            if create_admin():
                print("Admin created, please ask them to verify their email")
            show_super_admin_menu()
        elif text == '2':
            pass
        elif text == '3':
            show_auth_menu()
        else:
            print("Invalid input, try again")


def show_admin_menu():
    while True:
        text = input("""
        1. Teacher management.
        2. Student management.
        3. Group management.
        4. Payment management.
        5. Logout.
        
        Choose an option above: """).strip()

        if text == '1':
            pass
        elif text == '2':
            pass
        elif text == '3':
            pass
        elif text == '4':
            pass
        else:
            print("Invalid input, try again")


def show_auth_menu():
    text = """
1. Log in.
2. Exit.
"""
    print(text)

    user_input = input("Choose an option above: ").strip()

    if user_input == "1":
        login = input("Enter a login: ").strip()
        password = input("Enter a password: ").strip()
        if check_super_admin(login=login, password=password):
            show_super_admin_menu()
        elif check_admin(login=login, password=password):
            show_admin_menu()
        else:
            print("System cannot detect you, please try later")
            show_auth_menu()
    elif user_input == "2":
        print("You quit the program!")
        return
    else:
        print("Invalid input, try again")
        show_auth_menu()


if __name__ == '__main__':
    show_auth_menu()
