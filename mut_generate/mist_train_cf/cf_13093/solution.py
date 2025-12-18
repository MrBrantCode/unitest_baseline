"""
QUESTION:
Create a function named `validate_email(email)` that takes a string as input and returns `True` if the string is a valid email address and `False` otherwise. The email address is valid if it meets the following conditions:
- The email address must have a maximum length of 50 characters.
- The local part (before the '@' symbol) must contain only alphanumeric characters, dots (.), underscores (_) and hyphens (-), and it cannot start or end with a dot, underscore or hyphen.
- The domain part (after the '@' symbol) must contain only alphanumeric characters and dots (.), and it cannot start or end with a dot.
- The domain part must have at least one dot (.) separating the domain name and the top-level domain.
- The top-level domain must be one of the following: .com, .org, .net, .edu, .gov.
"""

import re

def validate_email(email):
    if len(email) > 50:
        return False

    local_part, domain_part = email.split('@')

    if not re.match(r'^[a-zA-Z0-9][a-zA-Z0-9_.-]*[a-zA-Z0-9]$', local_part):
        return False

    if not re.match(r'^[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*\.(com|org|net|edu|gov)$', domain_part):
        return False

    return True