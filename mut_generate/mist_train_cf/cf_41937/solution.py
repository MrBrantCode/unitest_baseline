"""
QUESTION:
Create a function `extract_copy_commands` that takes a string of commands as input and returns a list of tuples containing the command number, source file path, and destination directory for copy commands. Each command is in the format `{command_number}) Copy <source_file_path> to <destination_directory>: cp <source_file_path> <destination_directory>`. Assume the input string is well-formatted and source file paths and destination directories do not contain spaces.
"""

from typing import List, Tuple

def extract_copy_commands(input_string: str) -> List[Tuple[int, str, str]]:
    commands = []
    lines = input_string.split('\n')
    for line in lines:
        parts = line.split(':')
        if len(parts) == 2:
            command_number, copy_command = parts[0].split(') Copy ')
            source_file_path, destination_directory = copy_command.split(' to ')
            commands.append((int(command_number), source_file_path.strip(), destination_directory.strip()))
    return commands