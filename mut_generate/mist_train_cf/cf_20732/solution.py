"""
QUESTION:
Write a function `email_pattern` that constructs a regular expression pattern in Python to match all valid email addresses, excluding any emails with the domains "gmail.com" and "yahoo.com".
"""

import re

def email_pattern(email):
    pattern = r"^(?!.*@(?:gmail|yahoo)\.com).*@.*$"
    return bool(re.match(pattern, email))