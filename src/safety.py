import pathlib

from src.exceptions import OutOfWorkingDirectory


def check_inside_working_directory(path : str | pathlib.Path):
    working_directory_path = pathlib.Path(".").resolve()
    path = pathlib.Path(path).resolve()

    if path.is_relative_to(working_directory_path):
        return
    raise OutOfWorkingDirectory("[Warning] The given path is outside of allowed workspace")