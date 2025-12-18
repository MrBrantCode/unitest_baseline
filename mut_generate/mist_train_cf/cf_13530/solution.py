"""
QUESTION:
Write a SQL expression to output all valid email addresses from a table of users where the email addresses must meet the following criteria:

- The email address must be in the format "username@domain.com".
- The username can only contain alphanumeric characters, underscore, dot, and hyphen.
- The domain name can only contain alphanumeric characters and dot, and it must have at least one dot.
- The email address must have a valid top-level domain (TLD).
- The email address must not exceed a total length of 255 characters.

Do not use regular expressions for this task.
"""

import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9.]+\.[a-zA-Z0-9]+$'
    if len(email) > 255:
        return False
    return bool(re.match(pattern, email))