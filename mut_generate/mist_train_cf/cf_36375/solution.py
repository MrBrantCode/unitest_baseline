"""
QUESTION:
Given a sequence of file system commands, determine the final directory after executing all commands. The commands can be either `cd <directory>` to move into a directory or `fi` to move up one level. Write a function `final_directory(initial_directory: str, commands: List[str]) -> str` that takes the initial directory and the sequence of commands as input and returns the final directory.
"""

from typing import List

def entrance(initial_directory: str, commands: List[str]) -> str:
    current_directory = initial_directory.split('/')
    for command in commands:
        if command == "fi":
            current_directory = current_directory[:-1]  
        else:
            _, directory = command.split()  
            if directory != "..":
                current_directory.append(directory)  
            else:
                current_directory = current_directory[:-1]  
    return '/'.join(current_directory)