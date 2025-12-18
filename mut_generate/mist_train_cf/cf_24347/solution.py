"""
QUESTION:
Construct a regular expression to validate an email address. The function should be able to check for the presence of alphanumeric characters, special characters '.', '+', '-', '_', '@', and a domain with at least two and at most four alphabetic characters. The email address should start with alphanumeric characters or special characters '.', '+', '-', '_', and end with the domain.
"""

import re

def validate_email(email):
    pattern = r"^[A-Za-z0-9\.\'\+\-\_]+(\@)[A-Za-z0-9.-]+([\.][a-zA-Z]{2,4})+$"
    if re.match(pattern, email):
        return True
    else:
        return False