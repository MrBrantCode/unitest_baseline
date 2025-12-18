"""
QUESTION:
Create a function `validate_email(email)` that takes an email address as input and returns `True` if the email is valid and `False` otherwise. The function should use a regular expression pattern to validate the email address and handle common edge cases such as multiple '.' characters, special characters (excluding '@' and '.'), and ensuring there's a domain extension after the last '.' character.
"""

import re

def validate_email(email):
    pattern = r"[^@]+@[^@]+\.[^@]+"
    if re.match(pattern, email):
        return True
    else:
        return False