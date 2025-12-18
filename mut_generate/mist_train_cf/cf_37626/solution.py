"""
QUESTION:
Implement the `get_command_full` and `get_reply_data` functions. 

You are given a dictionary `_instruction_fields_key` that maps command types to their respective indices in the `command_full` list, and the `command_full` list containing the full details of each command. 

The `get_command_full` function should take a command name as input and return the full details of the command. 

The `get_reply_data` function should take a command name as input and return the reply data associated with that command.
"""

def get_command_full(name, command_full):
    """Returns the full details of the command based on the given name."""
    for command in command_full:
        if command[0] == name:
            return command

def get_reply_data(name, command_full):
    """Returns the reply data associated with the given command name."""
    for command in command_full:
        if command[0] == name:
            return command[1]