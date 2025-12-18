"""
QUESTION:
Create a function `is_valid_email(email)` that uses regular expressions to validate whether a given email address is in the correct format. The function should return `True` if the email is valid and `False` otherwise. The regular expression pattern should follow a simplified version of the RFC 5322 standard for email addresses, which requires the email to have a username, domain, and top-level domain.
"""

import re

def is_valid_email(email):
    """
    Returns True if the given email is a valid email address, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None