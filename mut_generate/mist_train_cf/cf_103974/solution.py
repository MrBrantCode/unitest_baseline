"""
QUESTION:
Write a function `check_name` that takes a string `name` as input and returns `True` if the name is exactly 5 characters long and starts with an uppercase letter, and `False` otherwise.
"""

def check_name(name):
    return len(name) == 5 and name[0].isupper()