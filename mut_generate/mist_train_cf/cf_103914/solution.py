"""
QUESTION:
Create a function named `check_string` that takes a string as input and returns `True` if the string contains only alphanumeric characters and has a minimum length of 5 characters. Otherwise, return `False`.
"""

import re

def check_string(string):
    return len(string) >= 5 and re.match(r'^[a-zA-Z0-9]+$', string)