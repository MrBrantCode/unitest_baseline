"""
QUESTION:
Create a function `validate_name_input(name)` that takes a string `name` as input and returns a string indicating whether the input is valid or not. The function should check if the input is not empty and contains only alphabetic characters. If the input is invalid, return a specific error message. If the input is valid, return "Name is valid".
"""

import re

def validate_name_input(name):
    if not name:
        return "Name is required"
    if not re.match("^[a-zA-Z]+$", name):
        return "Name should contain only alphabetic characters"
    return "Name is valid"