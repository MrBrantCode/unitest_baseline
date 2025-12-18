"""
QUESTION:
Create a function called `replace_emails_with_EMAIL(s)` that takes a string `s` as input and returns the string with all email addresses replaced with "EMAIL". The function should use regular expressions to identify the email addresses.
"""

import re

def replace_emails_with_EMAIL(s):
    return re.sub(r'\S+@\S+', 'EMAIL', s)