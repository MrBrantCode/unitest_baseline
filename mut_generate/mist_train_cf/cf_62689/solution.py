"""
QUESTION:
Create a function named `parse_command` that uses Python's regex module to interpret user commands in a simple text-based game. The function should be able to parse two types of commands: "look" and "use". The "look" command should describe the lamp's state, and the "use" command should toggle the lamp's state. The function should print the lamp's state or an error message when an invalid command is entered. Assume the lamp's initial state is off.
"""

import re

def parse_command(command, lamp_on):
    commands = {
        'look': lambda args: print("There's a lamp here. It's on." if lamp_on and 'lamp' in args else "There's a lamp here. It's off." if 'lamp' in args else "You're in a room. There's a table with a lamp on it." if 'room' in args else 'I do not understand that command.'),
        'use': lambda args: print("The lamp is already on." if lamp_on and 'lamp' in args else "You turned the lamp on." if 'lamp' in args else 'I do not understand that command.') if 'use' in command else None
    }
    
    for cmd, action in commands.items():
        if re.match(cmd, command):
            if cmd == 'use' and 'lamp' in command:
                return True
            action(command.split())
            return lamp_on
    print('I do not understand that command.')
    return lamp_on