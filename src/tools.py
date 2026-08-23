import os
import pathlib
from typing import Literal

from nexus.tool_registry import ToolRegistry
from dotenv import load_dotenv
from src.safety import check_inside_working_directory
from src.share import model, client

load_dotenv()

tool_registry = ToolRegistry()




@tool_registry.add_tool()
def semantic_search(query : str):
    result = client.query_points(collection_name=os.environ["COLLECTION_NAME"], query=model.encode(query), limit=3).points
    return [[data.payload, data.score] for data in result]


@tool_registry.add_tool()
def list_folder_items(folder_path : str = "."):
    """You to get the items inside the folder. by default it get current working directory items"""
    path = pathlib.Path(folder_path)
    if not path.exists():
        return "[ERROR] : The give file path doesn't exists!"
    if path.is_file():
        return "[ERROR] : The given path point to type file. please give a valid path that points to a folder"
    check_inside_working_directory(path=path)
    contents = []
    for content_path in path.glob("*"):
        contents.append(str(content_path.absolute()))
    return contents

@tool_registry.add_tool()
def read_file(file_path : str):
    "Use to read contents of a give file"
    path = pathlib.Path(file_path)
    if not path.exists():
        return "[ERROR] : The give file path doesn't exists!"
    if not path.is_file():
        return "[ERROR] : The given path doesn't point to type file. please give a valid path that points to a file"
    check_inside_working_directory(path=path)
    with open(path, "r", encoding="utf-8") as file:
        file_content = ""
        file_line_content = file.readlines()
        for index, line in enumerate(file_line_content):
            file_content += f"{index}\t{line}"
        if file_content == "":
            return "[NOTICE] File Empty."
        return file_content.encode().decode()

@tool_registry.add_tool()
def edit_file(file_path : str, index : int ,content : str, operation : str):
    """Used when small changes or edit need to be made to a file
    Parameters:
        file_path : path to file to be edited
        index : line to be edited
        content : text to be added to file
        operation : options > [replace, append]
    """

    path = pathlib.Path(file_path)
    if not path.exists():
        return "[ERROR] : The give file path doesn't exists!"
    if not path.is_file():
        return "[ERROR] : The given path doesn't point to type file. please give a valid path that points to a file"
    check_inside_working_directory(path=path)
    with open(path, "r", encoding="utf-8") as file:
        file_line_content = file.readlines()
        if index >= len(file_line_content):
            return "[ERROR] : Out of existing file lines scope"
    match operation:
        case "append":
            file_line_content.insert(index, content)
        case "replace":
            file_line_content[index] = content
        case _:
            return "[ERROR] : Unsupported Operation. Supported : [append , replace]"
    with open(path, "w", encoding="utf-8") as file:
        file.write("".join(file_line_content))
    return "[PASSED] Successfully applied changes"

@tool_registry.add_tool()
def remove_file_line(file_path : str, index : int):
    path = pathlib.Path(file_path)
    if not path.exists():
        return "[ERROR] : The give file path doesn't exists!"
    if not path.is_file():
        return "[ERROR] : The given path doesn't point to type file. please give a valid path that points to a file"
    check_inside_working_directory(path=path)
    with open(path, "r", encoding="utf-8") as file:
        file_line_content = file.readlines()
        if index > len(file_line_content):
            return "[ERROR] : Out of existing file lines scope"
    file_line_content.pop(index)
    with open(path, "w", encoding="utf-8") as file:
        file.write("".join(file_line_content))
    return "[PASSED] Successfully applied changes"

@tool_registry.add_tool()
def write_file(file_path : str, content : str, over_write : bool):
    "Used to write content into given file"

    path = pathlib.Path(file_path)
    if not path.exists():
        return "[ERROR] : The give file path doesn't exists!"
    if not path.is_file():
        return "[ERROR] : The given path doesn't point to type file. please give a valid path that points to a file"
    check_inside_working_directory(path=path)
    with open(path, "w" if over_write else "a", encoding="utf-8") as file:
        file.write(content)
    return "[PASSED] Successfully applied changes"