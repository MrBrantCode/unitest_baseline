"""
QUESTION:
Create a function `check_upper` that takes a string as input and returns `True` if the string contains at least one uppercase letter, and `False` otherwise. The function should check all characters in the string.
"""

def check_upper(string):
    if any(char.isupper() for char in string):
        return True
    return False