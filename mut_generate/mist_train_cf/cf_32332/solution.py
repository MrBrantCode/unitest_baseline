"""
QUESTION:
Write a function `final_directory` that takes a list of strings representing a sequence of commands and returns the final directory that the CLI would be in after executing the commands. The function should support "cd" to change the current directory and "exit" to terminate the program. The "cd" command takes a single argument representing the directory to change to. Directories are represented as strings, and the ".." string denotes moving up one level in the directory hierarchy. Assume that the initial directory is the root directory and that attempting to move up from the root directory has no effect.
"""

from typing import List

def final_directory(commands: List[str]) -> str:
    current_directory = "/"
    for command in commands:
        if command == "exit":
            return current_directory
        elif command.startswith("cd"):
            next_directory = command.split(" ")[1]
            if next_directory == "..":
                if current_directory != "/":
                    current_directory = "/".join(current_directory.split("/")[:-1])
            else:
                current_directory = current_directory + "/" + next_directory
    return current_directory