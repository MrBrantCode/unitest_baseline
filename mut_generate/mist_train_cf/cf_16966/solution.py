"""
QUESTION:
Write a function `is_valid_hexadecimal` that checks if a given string is a valid hexadecimal number with a '0x' prefix. The string must start with '0x' and only contain digits 0-9 and letters A-F (case-insensitive). Return True if the string is valid, False otherwise.
"""

def is_valid_hexadecimal(string):
    if not string.startswith('0x'):
        return False

    hexadecimal = string[2:].upper()

    for char in hexadecimal:
        if not (char.isdigit() or ('A' <= char <= 'F')):
            return False

    return True