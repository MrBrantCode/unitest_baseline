"""
QUESTION:
Create a function called `validate_email` that takes a string as input and returns True if the string matches a common email format (a string of alphanumeric characters, including ., %, +, -) followed by @, followed by another string of alphanumeric characters, a dot, and a top-level domain like 'com', 'edu', 'gov', etc. The function should be case-sensitive and should not allow quoted strings and special characters.
"""

import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.search(pattern, email))