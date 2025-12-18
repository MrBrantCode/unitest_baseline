"""
QUESTION:
Create a function `validate_string` that checks if the input string contains any numbers, special characters, or whitespace characters and returns `False` if it does, and `True` otherwise. The function should only consider printable characters that are letters (both upper and lower case) as valid.
"""

import re

def validate_string(s):
    pattern = r'[^a-zA-Z]'  # Matches any character that is not a letter
    if re.search(pattern, s):
        return False
    else:
        return True