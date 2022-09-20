from datetime import datetime


class Log:
    def __init__(self) -> None:
        pass

    def write_log(self, message: str) -> bool:
        try:
            file = open("log.txt", "a")
            file.write(
                f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')} // {message}\n")
            return True
        except Exception as e:
            file = open("log.txt", "a")
            file.write(
                f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')} // Error {e}\n")
            return False
