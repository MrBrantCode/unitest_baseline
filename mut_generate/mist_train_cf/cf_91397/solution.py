"""
QUESTION:
Create a function `is_integer(string)` that validates if a given string is an integer. The string can be preceded by an optional positive or negative sign, contain leading and trailing whitespaces, and must consist of only digits. The string cannot exceed a length of 10 characters, cannot start with leading zeros (except for the case where the string only contains the digit zero), and cannot be an empty string. The function should return `True` if the string is a valid integer and `False` otherwise.
"""

def is_integer(string):
    string = string.strip()
    
    # Check if string is empty
    if len(string) == 0:
        return False
    
    # Check if string starts with a sign
    if string[0] == '+' or string[0] == '-':
        string = string[1:]
    
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