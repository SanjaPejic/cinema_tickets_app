from models.role import Role


class User:
    def __init__(self, username: str, password: str, name: str, surname: str, role: Role):
        self.username = username
        self.password = password
        self.name = name
        self.surname = surname
        self.role = role
