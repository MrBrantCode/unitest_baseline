"""
QUESTION:
Construct a regular expression pattern to match email addresses affiliated with the domain "example.com" and write a function `find_emails(text)` that returns all matches from the input `text`. The email address should start with one or more alphanumeric characters or special characters `.`, `_`, `%`, `+`, `-` followed by `@example.com`. The function should use the `re` module in Python and return a list of matched email addresses.
"""

import re

def find_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@example\.com\b'
    return re.findall(pattern, text)