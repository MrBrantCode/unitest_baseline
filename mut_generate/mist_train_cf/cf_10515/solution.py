"""
QUESTION:
Write a function called `is_integer` that takes a string as input and returns `True` if the string represents a valid integer, and `False` otherwise, under the following conditions:
- The string can start with an optional '+' or '-' sign.
- The string can have leading and trailing whitespaces.
- The string must only consist of digits.
- The string's length cannot exceed 10 characters.
- The string cannot start with leading zeros unless the string only contains the digit zero.
- The string cannot be empty.
"""

def is_integer(string):
    string = string.strip()  # Remove leading and trailing whitespaces
    
    # Check if string is empty
    if len(string) == 0:
        return False
    
    # Check if string starts with a sign
    if string[0] == '+' or string[0] == '-':
        string = string[1:]  # Remove sign from the string
    
    # Check if string contains only digits
    if not string.isdigit():
        return False
    
    # Check if string exceeds length of 10 characters
    if len(string) > 10:
        return False
    
    # Check if string starts with leading zeros
    if string[0] == '0' and len(string) > 1:
        return False
    
    return True