"""
QUESTION:
Write a function `is_empty` that takes a string as input and returns `True` if the string is empty, contains only whitespace characters, or contains only special characters, and `False` otherwise. The function should ignore leading and trailing whitespace characters when checking if the string is empty.
"""

def is_empty(string):
    string = string.strip()
    return len(string) == 0 or all(not char.isalnum() for char in string)