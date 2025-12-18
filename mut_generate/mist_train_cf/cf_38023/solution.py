"""
QUESTION:
Implement a function `simulate_file_system(commands)` that simulates the behavior of a command-line tool for deleting files and directories. The function takes a list of commands as input, where each command is a string representing a file or directory operation. The supported operations are `rm <file>` to remove a file and `rm -rf <directory>` to remove a directory and its contents recursively. The function should handle the commands in the order they are given and return the final state of the file system after executing all the commands.

The initial state of the file system is as follows: `file1`, `file2`, `directory1/`, `directory1/file3`, `directory1/file4`, `directory2/`, `directory2/file5`. The function should return the final state of the file system as a list of files and directories.
"""

from typing import List

def entance(commands: List[str]) -> List[str]:
    file_system = {
        "file1",
        "file2",
        "directory1/",
        "directory1/file3",
        "directory1/file4",
        "directory2/",
        "directory2/file5"
    }

    for command in commands:
        if command.startswith("rm -rf"):
            directory = command.split(" ")[-1]
            to_remove = [item for item in file_system if item.startswith(directory)]
            file_system.difference_update(to_remove)
        elif command.startswith("rm"):
            file_system.discard(command.split(" ")[-1])

    return sorted(list(file_system))