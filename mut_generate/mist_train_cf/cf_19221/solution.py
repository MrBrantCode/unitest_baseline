"""
QUESTION:
Create a Python function `validate_name` that takes a string `name` as input and returns `True` if the name consists of alphabetical characters only and `False` otherwise. Use this function in a while loop that continuously prompts the user for input until they enter "exit". If the input name is valid, print "Hello, [name]!" where [name] is the user's input. If the input name is invalid, display an error message and prompt for input again. The function should be case-insensitive when checking for "exit".
"""

import re

def validate_name(name):
    pattern = re.compile('[^a-zA-Z]')
    if pattern.search(name):
        return False
    return True