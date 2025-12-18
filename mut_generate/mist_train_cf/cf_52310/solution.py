"""
QUESTION:
Create a function `extract_email` that takes a string `document` as input and returns all the email addresses present in the string. The function should be able to match standard email address formats.
"""

import re

def extract_email(document):
    pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
    return re.findall(pattern, document)