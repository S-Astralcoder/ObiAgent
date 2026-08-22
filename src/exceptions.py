class OutOfWorkingDirectory(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class InvalidWorkingDirectory(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)