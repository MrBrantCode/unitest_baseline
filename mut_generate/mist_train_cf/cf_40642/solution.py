"""
QUESTION:
Implement a function called `validate_switches` that takes a dictionary of switches and their values as input. The function should return a list of valid switches. A valid switch is defined as a key-value pair where the key starts with "--" and the value is not an empty string.
"""

def validate_switches(switches):
    valid_switches = [key for key, value in switches.items() if key.startswith("--") and value]
    return valid_switches