"""
QUESTION:
Implement the function `process_commands(commands: List[str]) -> List[str]` that processes a list of strings representing commands and their arguments. The function should execute the commands and return the final state of a system based on the commands executed. 

The function should handle four types of commands: "add", "remove", "update", and "execute". The "add" command adds an item to the system, the "remove" command removes an item from the system (if it exists), the "update" command updates an existing item in the system, and the "execute" command finalizes the commands and returns the current state of the system.

The system starts empty, and the commands should be executed in the order they appear in the input list. The function should return a list of strings representing the final state of the system after executing all the commands.
"""

from typing import List

def process_commands(commands: List[str]) -> List[str]:
    system_state = []
    for command in commands:
        action, *args = command.split()
        if action == "add":
            system_state.append(args[0])
        elif action == "remove":
            if args[0] in system_state:
                system_state.remove(args[0])
        elif action == "update":
            if args[0] in system_state:
                index = system_state.index(args[0])
                system_state[index] = args[1]
        elif action == "execute":
            return system_state
    return system_state