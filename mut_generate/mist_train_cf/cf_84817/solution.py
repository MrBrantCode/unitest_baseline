"""
QUESTION:
Create a function named `get_gmail_addresses` that takes a string `text` as input and returns all email addresses associated with the domain `gmail.com` using a regular expression. The function should handle standard email address formats, but does not need to account for all possible valid email address variations.
"""

import re

def get_gmail_addresses(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@gmail\.com\b'
    return re.findall(pattern, text)