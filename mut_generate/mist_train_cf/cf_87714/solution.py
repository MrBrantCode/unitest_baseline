"""
QUESTION:
Write a function `is_empty` that takes a string as input, ignores leading and trailing whitespace characters, and returns `True` if the string is empty, contains only whitespace characters, or contains only special characters. The function should return `False` otherwise. The function should handle cases where the string contains only whitespace characters or only special characters.
"""

def is_empty(string):
    string = string.strip()
    if len(string) == 0:
        return True
    for char in string:
        if not char.isspace() and not char.isalnum():
            return True
    return False