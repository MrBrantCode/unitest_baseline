"""
QUESTION:
Create a function `email_match(email)` that returns `True` if the input email address starts with a digit, includes at least one underscore (_) and one hyphen (-) in the username part, and ends with either `.org`, `.net`, or `.edu`, and `False` otherwise.
"""

import re

def email_match(email):
    pattern = r'^[0-9][a-zA-Z0-9\-\_]+@[a-zA-Z0-9\-]+\.(org|net|edu)$'
    if re.search(pattern, email):
        return True
    else:
        return False