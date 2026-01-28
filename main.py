import sys

from models.role import Role
from models.user import User

user_first = User("sanjapejic", "1234A", "Sanja", "Pejic", Role.CUSTOMER)
print(f"User's full name is: {user_first.name} {user_first.surname}")
print(f"User's role is: {user_first.role}")

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
        print(f"File is not found, {e} ")

    return data_matrix


def check_existing_user(username: str, password: str) -> User:
    data_matrix = load_data()
    for row in data_matrix:
        if username == row[0] and password == row[1]:
            return User(username,password, row[2], row[3], row[4])
    return None


def login() -> User:
    while True:
        username = input("\nInput Username: ").strip()
        password = input("Input password: ").strip()
        user = check_existing_user(username, password)

        if user is not None:
            break
        print("Wrong username or password. Try again.")

    print(f"\n{username}, successful login")
    return user


def register() -> User:
    username = input("Create a username: ")
    password = input("Create a password: ")
    name = input("Input name: ")
    surname = input("Input surname: ")
    print("Your role is a customer.")
    new_user = User(username, password, name, surname, Role.CUSTOMER)
    print(f"{username} is successfully created")
    return new_user


def display_auth_menu() -> User:
    while True:
        print("\nStart")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Choose 1 or 2: ").strip()

        if choice == "1":
            return login()
        elif choice == "2":
            return register()
        elif choice == "3":
            print("\nExiting the program...")
            sys.exit()
        else:
            print("\nInvalid choice. Enter number 1 or number 2 or 3.")


def display_user_menu(user: User):
    print("\nMain Menu")
    print("1. ")
    print("2. ")
    print("3. ")
    print("4. ")
    print("5. Exit")


if __name__ == '__main__':
    user = display_auth_menu()
    print(f"\nWelcome {user.name} {user.surname}!")
    display_user_menu(user)

