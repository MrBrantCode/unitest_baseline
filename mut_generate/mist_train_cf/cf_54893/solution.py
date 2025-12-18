"""
QUESTION:
Write a function called `find_emails` that takes a string `text` as input and returns a list of all email addresses found in the text. The function should use regular expressions to identify the email addresses. The email addresses may be embedded within varying contexts in the text. The function should match most common email address formats, but does not need to cover all possible valid email addresses.
"""

import re

def find_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return re.findall(pattern, text)