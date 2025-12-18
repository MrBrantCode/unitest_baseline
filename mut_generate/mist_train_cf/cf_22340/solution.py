"""
QUESTION:
Write a function `check_string` that takes a string of alphanumeric characters as input and returns a boolean value indicating whether the string contains exactly two consecutive digits and at least one uppercase letter.
"""

import re

def check_string(string):
    pattern = r'^(?=.*[A-Z])(?=.*\d{2})[A-Za-z\d]+$'
    return bool(re.match(pattern, string))