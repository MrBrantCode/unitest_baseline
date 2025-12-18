"""
QUESTION:
Validate a given string as an integer with the following constraints: the string can be preceded by an optional '+' or '-' sign, contain leading/trailing whitespaces, and consist of digits only, but cannot exceed 10 characters, start with leading zeros (unless it's '0'), or be empty. The function should have a time complexity of O(n), where n is the string length, and not use built-in string-to-integer conversion functions or libraries. Implement the validation code in a programming language of your choice and return a boolean value indicating whether the string is a valid integer or not.
"""

def entrance(s: str) -> bool:
    if len(s) == 0:
        return False

    s = s.strip()
    if len(s) > 10:
        return False

    if s[0] == '+' or s[0] == '-':
        s = s[1:]

    if len(s) == 0:
        return False

    if s[0] == '0' and len(s) > 1:
        return False

    for char in s:
        if not char.isdigit():
            return False

    return True