"""
QUESTION:
Create a function named `find_control_chars` that takes a string as input and returns a boolean value indicating whether the string contains any control characters. The control characters to be detected are carriage return (`\r`) and newline (`\n`).
"""

def find_control_chars(s):
    control_chars = [
        '\r', 
        '\n'
    ]
    for char in control_chars:
        if char in s:
            return True
    return False