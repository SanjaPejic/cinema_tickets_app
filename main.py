import sys

from models.role import Role
from models.user import User

# user_first = User("sanjapejic", "1234A", "Sanja", "Pejic", Role.CUSTOMER)
# print(f"User's full name is: {user_first.name} {user_first.surname}")
# print(f"User's role is: {user_first.role}")

data_file_path = "user_data.txt"


def load_data() -> []:
    data_matrix = []
    try:
        with open(data_file_path, mode="r") as data_file:
            data_lines = data_file.readlines()
        data_lines.pop(0)

        for line in data_lines:
            row = line.strip().split("|")
            data_matrix.append(row)

    except FileNotFoundError as e:
        print(f"File not found: {e} ")

    return data_matrix


def check_existing_user(username: str, password: str) -> User | None:
    data_matrix = load_data()
    for row in data_matrix:
        if username == row[0] and password == row[1]:
            try:
                role = Role(row[4])
            except ValueError:
                print("Invalid role in the data file.")
                print("Defaulting to customer.")
                role = Role.CUSTOMER
            return User(username,password, row[2], row[3], role)
    return None


def login() -> User:
    while True:
        username = input("\nEnter Username: ").strip()
        password = input("Enter password: ").strip()
        found_user = check_existing_user(username, password)

        if found_user is not None:
            break
        print("Invalid login. Try again.")

    print(f"Login successful, {username}")
    return found_user


def register() -> User | None:

    unique = False
    while not unique:
        username = input("Create a username: ")
        data_matrix = load_data()
        unique = True
        for line in data_matrix:
            if line[0] == username:
                unique = False
                print("The username already exists. Try again.")

    password = ""
    has_digit = False
    is_long = False
    while not (has_digit and is_long):
        password = input("Create a password: ")
        if len(password) >= 7:
            is_long = True
        else:
            print("Use at least 7 characters. Try again.")
        for char in password:
            if char.isdigit():
                has_digit = True
        if not has_digit:
            print("Include at least one digit. Try again.")

    name = input("Enter your first name: ")
    surname = input("Enter your surname: ")

    try:
        with open(data_file_path, mode="a+") as data_file:
            data_file.write(f"\n{username}|{password}|{name}|{surname}|{Role.CUSTOMER}")
            new_user = User(username, password, name, surname, Role.CUSTOMER)
            print("Assigned role: customer.")
            print(f"Account created: {username}.")
            return new_user

    except FileNotFoundError as e:
        print(f"File not found, {e} ")

    return None


def display_auth_menu() -> User:
    while True:
        print("-----------------Start-----------------")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        print("---------------------------------------")
        choice = input("Choose 1, 2, or 3: ").strip()

        if choice == "1":
            return login()
        elif choice == "2":
            return register()
        elif choice == "3":
            print("\nExiting the program...")
            sys.exit()
        else:
            print("\nInvalid choice. Enter 1, 2, or 3.")


def display_user_menu(user: User):
    print("---------------------------------------------------------------------------")
    print(f"Main Menu: {user.username}")
    print("1. ")
    print("2. ")
    print("3. ")
    print("4. ")
    print("5. Exit")
    print("---------------------------------------------------------------------------")


if __name__ == '__main__':
    logged_user = display_auth_menu()
    print(f"\nWelcome, {logged_user.name} {logged_user.surname}!")
    display_user_menu(logged_user)

