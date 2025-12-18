"""
QUESTION:
Write a function `parseCommand(command: str) -> dict` that takes a string `command` as input, representing a command-line instruction with a program name followed by one or more options or arguments, each preceded by a hyphen (-) and separated by spaces. The function should return a dictionary containing the program name, options, and arguments with keys "program", "options", and "arguments" respectively, where "options" and "arguments" are lists of strings. Assume that the input command is well-formed.
"""

def parseCommand(command: str) -> dict:
    parts = command.split()
    program = parts[0]
    options = [part for part in parts[1:] if part.startswith('-')]
    arguments = [part for part in parts[1:] if not part.startswith('-')]
    return {
        "program": program,
        "options": options,
        "arguments": arguments
    }