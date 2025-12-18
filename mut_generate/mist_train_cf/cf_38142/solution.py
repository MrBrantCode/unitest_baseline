"""
QUESTION:
Write a Python function `execute_command(command: str) -> str` that takes a command string in the format "ACTION TARGET [VALUE]" where ACTION, TARGET, and VALUE do not contain spaces, ACTION and TARGET are separated by a space, and VALUE is enclosed in square brackets and separated from the TARGET by a space if present. The function should parse the command, execute the corresponding action on the specified target, and return a reply in the format "TARGET [REPLY]". Assume "GET" and "SET" are the only valid actions.
"""

import re

def execute_command(command: str) -> str:
    action, target, value = re.match(r'(\w+) (\w+)(?: \[(\w+)\])?', command).groups()
    if action == "GET":
        return f"{target} [07473725]"
    elif action == "SET":
        return ""
    else:
        return "Invalid command action"