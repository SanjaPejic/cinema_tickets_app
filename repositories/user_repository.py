from models.role import Role
from models.user import User
from utils.logger import Logger

USER_FILE_PATH = "user_data.txt"


def load_user_data() -> list[list[str]]:
    data_matrix: list[list[str]] = []
    try:
        with open(USER_FILE_PATH, mode="r") as data_file:
            data_lines = data_file.readlines()
        data_lines.pop(0)

        for line in data_lines:
            row = line.strip().split("|")
            if len(row) != 5:
                Logger.error("Skipping invalid user row (wrong number of fields).")
                continue
            data_matrix.append(row)

    except FileNotFoundError as e:
        Logger.error(f"File not found: {e} ")

    return data_matrix


def check_existing_user(username: str, password: str) -> User | None:
    data_matrix = load_user_data()
    for row in data_matrix:
        if username == row[0] and password == row[1]:
            try:
                role = Role(row[4])
            except ValueError:
                Logger.error("Invalid role in the data file.\nDefaulting to customer.")
                role = Role.CUSTOMER
            return User(username, password, row[2], row[3], role)
    return None


def append_user(user: User) -> None:
    try:
        with open(USER_FILE_PATH, mode="a+") as data_file:
            data_file.write(f"\n{user.username}|{user.password}|{user.name}|{user.surname}|{user.role}")
    except FileNotFoundError as e:
        Logger.error(f"File not found, {e} ")