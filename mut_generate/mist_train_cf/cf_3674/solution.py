"""
QUESTION:
Create a function called `validate_string` that takes one argument `input_string`. The function should return `True` if the string only contains letters and return `False` otherwise. The function should be able to handle strings that contain numbers, special characters, whitespace characters, or any characters that are not letters, numbers, or special characters.
"""

import re

def validate_string(input_string):
    pattern = r'[^a-zA-Z]'
    if re.search(pattern, input_string):
        return False
    else:
        return True