"""
QUESTION:
Create a function called `validate_string` that takes a string as input and returns a boolean indicating whether the string matches the following criteria:

- The string is at least 6 characters long.
- The string contains at least one uppercase letter, one lowercase letter, and one number.
- The string does not contain the words "password" or "credit card".
- The string only contains alphanumeric characters (a-zA-Z0-9).

The function should also be able to handle strings in multiple languages, including Spanish and Mandarin Chinese.
"""

import re

def validate_string(s):
    """
    Validate a string based on the following criteria:
    - The string is at least 6 characters long.
    - The string contains at least one uppercase letter, one lowercase letter, and one number.
    - The string does not contain the words "password" or "credit card".
    - The string only contains alphanumeric characters (a-zA-Z0-9).
    
    Args:
        s (str): The string to be validated.
    
    Returns:
        bool: True if the string is valid, False otherwise.
    """
    pattern = r"^(?!.*(?:password|credit card))(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9]{6,}$"
    return bool(re.match(pattern, s))