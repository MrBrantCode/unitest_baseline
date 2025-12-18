"""
QUESTION:
Implement a function `execute_commands` that takes a list of commands as input and executes them in the order they appear in the list. Each command can be one of three types: `pip uninstall <package_name>`, `echo "<message>"`, or `apt-get purge <package_name> -y`. The function should return a list of messages printed to the console during the execution of the commands. The messages should include the package names for uninstall and purge operations and the specified message for echo operations.
"""

from typing import List

def execute_commands(commands: List[str]) -> List[str]:
    printed_messages = []
    for command in commands:
        if command.startswith('sudo pip uninstall'):
            package_name = command.split(' ')[3]
            printed_messages.append(f'Uninstalling package {package_name}')
        elif command.startswith('echo'):
            message = command.split('"')[1]
            printed_messages.append(message)
        elif command.startswith('sudo apt-get purge'):
            package_name = command.split(' ')[4]
            printed_messages.append(f'Purging package {package_name}')
    return printed_messages