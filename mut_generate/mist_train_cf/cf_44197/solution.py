"""
QUESTION:
Write a function `is_valid_email` that checks if an email address is valid. The email address is valid if it meets the following conditions: 
- it contains an "@" symbol and a "."
- it has at least 6 characters
- the local-part (before "@") contains only alphanumeric characters, hyphens, or underscores
- the domain name (after "@") contains only alphanumeric characters and hyphens
- the domain ending (after ".") has 2-6 alphanumeric characters
- the local-part has at least 2 characters and the domain name has at least 3 characters (excluding the domain ending)
"""

import re

def is_valid_email(email):
    # Create regex for a valid email address
    regex = r"^([a-zA-Z0-9_\.-]{2,})@([a-zA-Z0-9-]{3,})\.([a-zA-Z0-9]{2,6})$"

    if len(email) < 6:
        return False

    # Find match
    match = re.fullmatch(regex, email)

    # If match found
    if match:
        return True
    # If match not found
    else:
        return False