"""
QUESTION:
Write a function called "find_emails" that takes a string as input and returns all unique email addresses found in the string. The function should use a regular expression to match common email address formats.
"""

import re

def find_emails(s):
    return set(re.findall(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", s))