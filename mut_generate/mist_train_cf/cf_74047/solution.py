"""
QUESTION:
Create a function `find_email` that takes a string `text` as input and returns all occurrences of the exact email address "test@example.com" within the text, using a regular expression that matches the email address as a whole word.
"""

import re

def find_email(text):
    pattern = r'\btest@example\.com\b'
    match = re.findall(pattern, text)
    return match