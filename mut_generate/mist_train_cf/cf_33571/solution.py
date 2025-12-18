"""
QUESTION:
Create a function `parse_help_text(help_text: str) -> dict` that takes a string `help_text` as input, where each command is prefixed with a forward slash (/), may have additional parameters enclosed in angle brackets (< >), and is followed by its description on a separate line. The function should return a dictionary where the keys are the commands and the values are their corresponding descriptions.
"""

def parse_help_text(help_text: str) -> dict:
    commands = {}
    lines = help_text.split('\n')
    command = None
    description = ""
    for line in lines:
        line = line.strip()
        if line.startswith('/'):
            if command is not None:
                commands[command] = description.strip()
            command = line
            description = ""
        else:
            description += line + " "
    if command is not None:
        commands[command] = description.strip()
    return commands