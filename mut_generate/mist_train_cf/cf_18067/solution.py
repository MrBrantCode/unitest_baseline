"""
QUESTION:
Create a function named `check_string` that takes a string as input and returns `True` if the string meets the following conditions, and `False` otherwise. The string should start with a capital letter 'A' and end with a lowercase letter 'z'. It should contain at least one digit and one non-alphanumeric character. The length of the string should be between 10 and 20 characters.
"""

import re

def check_string(s):
    return s[0] == 'A' and s[-1] == 'z' and any(char.isdigit() for char in s) and any(not char.isalnum() for char in s) and 10 <= len(s) <= 20