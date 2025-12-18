"""
QUESTION:
Create a function called `is_empty` that takes a string as input. The function should return `True` if the string is empty after removing leading and trailing whitespace, and `False` otherwise.
"""

def is_empty(s):
    return len(s.strip()) == 0