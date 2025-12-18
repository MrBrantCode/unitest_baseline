"""
QUESTION:
Write a regular expression function `regex` that matches strings consisting of at least 3 digits, followed by any characters, and ending with a letter.
"""

import re

def regex(string):
    pattern = r"\d{3,}.*[a-zA-Z]$"
    return bool(re.match(pattern, string))