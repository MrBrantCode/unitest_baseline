"""
QUESTION:
Implement a function named `password` that takes a `user` (string) and `password` (string) as input and returns a tuple containing a `CommandLine` object and a callable function. The `CommandLine` object should be constructed using the provided `user` and `password` to execute a specific command. The callable function should take a string as input.
"""

from typing import Tuple, Callable

class CommandLine:
    def __init__(self, command: str):
        self.command = command

def password(user: str, password: str) -> Tuple[CommandLine, Callable[[str], None]]:
    command = f'powershell -command "&{{Write-Host \\"User: {user} | Password: {password}\\"}}"'
    def recover_files(directory: str) -> None:
        # Implement the file recovery logic based on the input directory
        pass
    return CommandLine(command), recover_files