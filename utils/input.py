from utils.logger import Logger


class Input:
    @staticmethod
    def get_int(input_message: str, error_message: str) -> int:
        while True:
            try:
                result_str = input(input_message).strip()
                if not result_str:
                    return 0
                return int(result_str)
            except ValueError:
                Logger.error(error_message)

    @staticmethod
    def get_required_text(message: str, error_message: str) -> str:
        while True:
            result_str = input(message).strip()
            if result_str:
                return result_str
            Logger.error(error_message)
