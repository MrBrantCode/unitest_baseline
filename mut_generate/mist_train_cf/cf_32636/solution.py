"""
QUESTION:
Implement the `verify_command` function, which takes four parameters: `command` (a list of strings representing the command), `config` (a dictionary mapping commands to their allowed and denied users), `user` (the user attempting to execute the command), and `command_type` (an enumeration of command types: `Allowed`, `Denied`, `Unknown`). The function should return the correct type of each command based on the provided configuration and user permissions.
"""

class CommandTypes:
    Allowed = 1
    Denied = 2
    Unknown = 3

def verify_command(command, config, user, command_type):
    if tuple(command) in config:
        allowed_users = config[tuple(command)].get('allowed', [])
        denied_users = config[tuple(command)].get('denied', [])
        if user in allowed_users:
            return command_type == CommandTypes.Allowed
        elif user in denied_users:
            return command_type == CommandTypes.Denied
        else:
            return command_type == CommandTypes.Unknown
    else:
        return command_type == CommandTypes.Unknown