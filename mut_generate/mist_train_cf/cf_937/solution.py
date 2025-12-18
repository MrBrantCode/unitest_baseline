"""
QUESTION:
Create a function `validate_string` that takes a string as input. The string should start with a lowercase letter, followed by any number of lowercase letters, numbers, and special characters, but cannot contain any consecutive duplicate characters. The string must end with a number. Return `True` if the string meets these conditions and `False` otherwise.
"""

import re

def validate_string(s):
    pattern = r"^[a-z](?!.*(.).*\1)[a-z0-9!@#$%^&*()-=_+;:',.<>/?]+[0-9]$"
    return bool(re.match(pattern, s))