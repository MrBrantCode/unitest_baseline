"""
QUESTION:
Write a function called 'match_domain' to match all email addresses that have the same top-level domain. The input is an email address string. The function should return True if the email address matches the pattern and False otherwise. The pattern should match one or more alphanumeric characters, dots, underscores, percent signs, plus signs, or hyphens, followed by an at symbol, followed by one or more alphanumeric characters, dots, or hyphens, followed by a dot, followed by the top-level domain (it should be 2 to 4 alphabetic characters).
"""

import re

def match_domain(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$"
    return bool(re.match(pattern, email))