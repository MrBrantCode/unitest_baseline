"""
QUESTION:
Create a function `check_string` that takes a string of alphanumeric characters as input and returns True if the string contains exactly two consecutive digits and at least one uppercase letter, False otherwise. The function should only match alphanumeric characters and must start and end with the entire string.
"""

import re

def check_string(string):
    pattern = r'^(?=.*[A-Z])(?=.*\d{2})[A-Za-z\d]+$'
    return bool(re.match(pattern, string))