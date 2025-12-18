"""
QUESTION:
Write a function `find_emails(text)` that takes a string `text` as input and returns a list of all email addresses found in the text using regular expressions. The function should handle email addresses with domain extensions of at least 2 characters long. The function should correctly extract email addresses even when they are followed by non-word characters, such as a period.
"""

import re

def find_emails(text):
    return re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text)