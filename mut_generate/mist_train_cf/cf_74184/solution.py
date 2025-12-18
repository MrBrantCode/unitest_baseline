"""
QUESTION:
Create a function named 'check_string' that uses a regular expression pattern to match a string. The string should start with 'hello', followed by two positive integer numbers separated by a comma and a space. The function should return True if the string matches the pattern and False otherwise. Ensure the numbers in the string are positive integers (greater than 0).
"""

import re

def check_string(string):
    pattern = r"^hello [1-9][0-9]*, [1-9][0-9]*$"
    return bool(re.match(pattern, string))