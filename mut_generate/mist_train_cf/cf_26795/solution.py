"""
QUESTION:
Write a function `process_arguments` that takes a list of strings as input, where each string represents a command followed by a key-value pair or a key separated by an equals sign ('='). The function should process the commands in order, updating a dictionary accordingly, and return the final state of the dictionary. 

The function should support the following commands: 
- `add=key=value`: Add a new key-value pair to the dictionary. If the key already exists, update its value.
- `remove=key`: Remove the specified key from the dictionary if it exists.
- `print`: Print the current state of the dictionary.

Note: The function should handle commands that are not 'add', 'remove', or 'print' as invalid and skip them.
"""

from typing import List, Dict

def process_arguments(args: List[str]) -> Dict[str, str]:
    attributes = dict()
    for arg in args:
        parts = arg.split('=')
        if len(parts) == 3 and parts[0] == 'add':
            attributes[parts[1]] = parts[2]
        elif len(parts) == 2 and parts[0] == 'remove':
            attributes.pop(parts[1], None)
        elif arg == 'print':
            print(attributes)
    return attributes