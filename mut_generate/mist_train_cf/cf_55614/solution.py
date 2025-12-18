"""
QUESTION:
Write a function `validate_name` that checks if a given name is valid based on a set of predefined patterns. The function should take a string as input and return `True` if the name is valid and `False` otherwise. A valid name consists of letters and spaces only. Additionally, write a function `get_name` that takes user input for their name and returns the input as a string. Use these functions to continually prompt the user for their name until a valid name is entered.
"""

import re

def validate_name(name):
    name_format = re.compile(r'^[A-Za-z\s]*$')
    if name_format.fullmatch(name):
        return True
    else:
        return False