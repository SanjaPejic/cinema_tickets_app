import sys


class Logger:
    @staticmethod
    def error(message: str) -> None:
        print(f"*** ERROR: {message} ***")
