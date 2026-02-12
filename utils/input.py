from enum import Enum

from utils.logger import Logger


class Input:
    @staticmethod
    def get_int_optional(input_message: str, error_message: str) -> int:
        while True:
            try:
                result_str = input(input_message).strip()
                if not result_str:
                    return 0
                return int(result_str)
            except ValueError:
                Logger.error(error_message)

    @staticmethod
    def get_int_required(message: str, error_message: str) -> int:
        while True:
            input_str = input(message).strip()
            if not input_str:
                Logger.error(error_message)
                continue
            try:
                return int(input_str)
            except ValueError:
                Logger.error(error_message)

    @staticmethod
    def get_required_text(message: str, error_message: str) -> str:
        while True:
            result_str = input(message).strip()
            if result_str:
                return result_str
            Logger.error(error_message)

    @staticmethod
    def get_enum_optional(message: str, enum_type: type[Enum], error_message:str) -> str:
        while True:
            input_str = input(message).strip().casefold()
            if input_str:
                try:
                    enum_type(input_str)
                except ValueError:
                    Logger.error(error_message)
                    continue
            return input_str

    @staticmethod
    def get_list_optional(message: str) -> list[str]:
        input_str = input(message).strip()
        if not input_str:
            return []
        return [s.strip() for s in input_str.split(",") if s.strip()]

    @staticmethod
    def get_text_optional(message: str) -> str:
        return input(message).strip()

    @staticmethod
    def get_int_range(message: str, min_value: int, max_value: int, error_message: str) -> int:
        while True:
            value = Input.get_int_required(message, "Enter a number using digits.")
            if min_value <= value <= max_value:
                return value
            Logger.error(error_message)
