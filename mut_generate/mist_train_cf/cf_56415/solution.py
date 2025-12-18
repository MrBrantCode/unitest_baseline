"""
QUESTION:
Write a function `verify_email(email)` that verifies the authenticity of an email address using a standard regular expression pattern. The function should ensure the proper format and structure, including validation of domains and subdomains, and special characters. The pattern should match the following conditions:
- Starts with at least one alphanumeric character (a-z or A-Z or 0-9).
- Can contain underscores (_) and periods (.) optionally.
- Contains at least one @ symbol after the first part.
- Ends with a domain that starts with at least one alphanumeric character (a-z), followed by a period and ends with 2 or 3 character-long domain type.
"""

import re

def verify_email(email):
    pattern = '[a-zA-Z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return bool(re.search(pattern, email))