"""
QUESTION:
Write a function called `validate_integer` that takes a string as input and returns a boolean value indicating whether the string is a valid integer. The string is considered a valid integer if it meets the following conditions: 
- It can be preceded by an optional positive or negative sign.
- It can contain leading and trailing whitespaces.
- It can only consist of digits.
- It cannot exceed a length of 10 characters.
- It cannot start with leading zeros, except for the case where the string only contains the digit zero.
- It cannot be an empty string.
The function should have a time complexity of O(n), where n is the length of the string, and should not use any built-in string-to-integer conversion functions or libraries.
"""

def validate_integer(string):
    if len(string) == 0:
        return False

    string = string.strip()
    if len(string) > 10:
        return False

    if string[0] == '+' or string[0] == '-':
        string = string[1:]

    if len(string) == 0:
        return False

    if string[0] == '0' and len(string) > 1:
        return False

    for char in string:
        if not char.isdigit():
            return False

    return True