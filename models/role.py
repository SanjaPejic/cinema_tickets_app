from enum import Enum


class Role(str, Enum):
    CUSTOMER = "customer"
    SELLER = "seller"
    MANAGER = "manager"

    def __str__(self):
        return self.value.lower()

