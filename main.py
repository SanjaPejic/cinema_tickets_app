import sys

from models.film import Film
from models.genre import Genre
from models.role import Role
from models.user import User

# user_first = User("sanjapejic", "1234A", "Sanja", "Pejic", Role.CUSTOMER)
# print(f"User's full name is: {user_first.name} {user_first.surname}")
# print(f"User's role is: {user_first.role}")

user_file_path = "user_data.txt"
film_file_path = "film_data.txt"


def load_user_data() -> list[list[str]]:
    data_matrix = []
    try:
        with open(user_file_path, mode="r") as data_file:
            data_lines = data_file.readlines()
        data_lines.pop(0)

        for line in data_lines:
            row = line.strip().split("|")
            data_matrix.append(row)

    except FileNotFoundError as e:
        print(f"File not found: {e} ")

    return data_matrix


def check_existing_user(username: str, password: str) -> User | None:
    data_matrix = load_user_data()
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
        data_matrix = load_user_data()
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
        with open(user_file_path, mode="a+") as data_file:
            data_file.write(f"\n{username}|{password}|{name}|{surname}|{Role.CUSTOMER}")
            new_user = User(username, password, name, surname, Role.CUSTOMER)
            print("Assigned role: customer.")
            print(f"Account created: {username}.")
            return new_user

    except FileNotFoundError as e:
        print(f"File not found, {e} ")

    return None


def load_film_data() -> list[Film]:
    film_list = []
    try:
        with open(film_file_path, mode="r") as data_file:
            file_lines = data_file.readlines()
        file_lines.pop(0)

        for line in file_lines:
            row = line.strip().split("|")
            if len(row) < 8:
                continue
            title = row[0]
            try:
                genre = Genre(row[1])
            except ValueError as e:
                genre = Genre.DRAMA
                print(f"Error {e}. Default genre given: drama")
            duration = int(row[2])
            directors = [d.strip() for d in row[3].split(",") if d.strip()]
            cast = [c.strip() for c in row[4].split(",") if c.strip()]
            country = row[5].strip()
            year = int(row[6])
            description = row[7]
            film = Film(title, genre, duration, directors, cast, country, year, description)
            film_list.append(film)

    except FileNotFoundError as e:
        print(f"File not found: {e} ")
    return film_list


def print_all_films(film_list: list[Film]) -> None:
    print("  | title | genre | duration_min | directors | main_cast | country | year | description")
    for i, film in enumerate(film_list):
        directors = ", ".join(film.directors)
        cast = ", ".join(film.cast)
        print(f"{i+1}."
              f"| {film.title} | {film.genre} | {film.duration} | {directors} "
              f"| {cast} | {film.country} | {film.year} | {film.description}")


def search_films_menu():
    print("Search for movie(s):")
    title = input("Title (leave empty to skip):")
    genre = input("Genre(leave empty to skip):")
    dur_min = input("Min duration in minutes (leave empty to skip):")
    dur_max = input("Max duration in minutes (leave empty to skip):")
    director = input("Director (leave empty to skip):")
    cast = input("Main cast member (leave empty to skip):")
    country = input("Country (leave empty to skip):")
    year = input("Year (leave empty to skip):")


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
    while True:
        print("---------------------------------------------------------------------------")
        print(f"Main Menu: {user.username}")
        print("1. See available movies")
        print("2. Search movies")
        print("3. ")
        print("4. ")
        print("5. Exit")
        print("---------------------------------------------------------------------------")
        choice = input("Choose a number from 1-5: ").strip()

        if choice == "1":
            print_all_films(load_film_data())
        elif choice == "2":
            search_films_menu()
        elif choice == "5":
            print("\nExiting the program...")
            sys.exit()
        else:
            print("\nInvalid choice. Enter a number from 1-5.")


if __name__ == '__main__':
    logged_user = display_auth_menu()
    print(f"\nWelcome, {logged_user.name} {logged_user.surname}!")
    display_user_menu(logged_user)

