import sys

from models.genre import Genre
from models.role import Role
from models.user import User
from repositories.film_repository import load_film_data
from repositories.user_repository import check_existing_user, append_user
from services.auth_service import get_unique_username, get_password
from services.film_service import print_films, search_films
from utils.input import Input


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


def register() -> User:
    username = get_unique_username()
    password = get_password()

    name = Input.get_required_text("Enter your first name: ", "First name cannot be empty")
    surname = Input.get_required_text("Enter your surname: ", "Surname cannot be empty")

    new_user = User(username, password, name, surname, Role.CUSTOMER)
    append_user(new_user)
    print("Assigned role: customer.")
    print(f"Account created: {new_user.username}.")

    return new_user


def search_films_menu() -> None:
    print("Search for movie(s):")
    title = input("Title (leave empty to skip): ").strip()
    genre = Input.get_enum_optional("Genre(exact, leave empty to skip): ", Genre,
                                    "Invalid genre. Use: action, comedy, drama, horror, romance or sci-fi.")

    dur_min = Input.get_int("Min duration in minutes (leave empty to skip): ",
                            "Enter a number using digits.")
    dur_max = Input.get_int("Max duration in minutes (leave empty to skip): ",
                            "Enter a number using digits.")

    directors = Input.get_list_optional("Directors (exact names, comma-separated, leave empty to skip): ")
    cast = Input.get_list_optional("Main cast (exact names, comma-separated, leave empty to skip): ")

    country = input("Country (exact, leave empty to skip): ").strip()

    year = Input.get_int("Year (leave empty to skip): ",
                         "Enter a number using digits.")

    print_films(search_films(title, genre, dur_min, dur_max, directors, cast, country, year))


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
            print_films(load_film_data())
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
