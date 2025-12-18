"""
QUESTION:
Create a function `is_uppercase_string` that takes a string as input and returns True if the string exclusively contains uppercase alphabetical letters, and False otherwise.
"""

import re

def is_uppercase_string(string):
    pattern = '^[A-Z]+$'
    if re.search(pattern, string):
        return True
    else:
        return False