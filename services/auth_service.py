from repositories.user_repository import load_user_data
from utils.input import Input
from utils.logger import Logger


def get_unique_username() -> str:
    while True:
        username = Input.get_required_text("Create a username: ", "Username cannot be empty")
        data_matrix = load_user_data()
        if any(row[0] == username for row in data_matrix):
            Logger.error("The username already exists. Try again.")
        else:
            return username


def get_password() -> str:
    while True:
        password = Input.get_required_text("Create a password: ", "Password cannot be empty. Try again")

        if len(password) < 7:
            Logger.error("Use at least 7 characters. Try again.")
            continue

        if not any(char.isdigit() for char in password):
            Logger.error("Include at least one digit. Try again.")
            continue

        return password
