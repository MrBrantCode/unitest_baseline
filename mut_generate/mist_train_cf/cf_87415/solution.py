"""
QUESTION:
Implement a function `is_valid_integer` that takes a string as input and returns a boolean value indicating whether the string is a valid integer. The string is a valid integer if it meets the following conditions:
- It can be preceded by an optional positive or negative sign.
- It can contain leading and trailing whitespaces.
- It can only consist of digits.
- It cannot exceed a length of 20 characters.
- It cannot start with leading zeros, except for the case where the string only contains the digit zero.
- It cannot be an empty string.
The function should have a time complexity of O(n), where n is the length of the string, and should not use any built-in string-to-integer conversion functions or libraries.
"""

def is_valid_integer(string):
    # Remove leading and trailing whitespaces
    string = string.strip()

    # Check if string is empty
    if len(string) == 0:
        return False

    # Check for optional positive or negative sign
    if string[0] == '+' or string[0] == '-':
        string = string[1:]

    # Check if string is empty after removing sign
    if len(string) == 0:
        return False

    # Check if string exceeds length limit
    if len(string) > 20:
        return False

    # Check if string only contains digits
    if not string.isdigit():
        return False

    # Check if string starts with leading zeros
    if len(string) > 1 and string[0] == '0':
        return False

    return True