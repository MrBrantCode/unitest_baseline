"""
QUESTION:
Implement the `is_valid_email` function, which takes a string as input and returns `True` if the input is a valid email address and `False` otherwise. A valid email address has the format `username@domain.extension`, where `username` can contain letters (a-z, A-Z), digits (0-9), dots (.), hyphens (-), and underscores (_), `domain` contains letters and digits only, and `extension` consists of 2-4 letters only. Do not use external libraries or modules for email validation.

Function signature: `def is_valid_email(email: str) -> bool`
"""

import re

def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}$'
    return bool(re.match(pattern, email))