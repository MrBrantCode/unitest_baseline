"""
QUESTION:
Create a function named `extract_email_addresses` that takes a string `text` as input and returns a list of all email addresses found in the text. The function should match most common email address formats.
"""

import re

def extract_email_addresses(text):
    email_reg = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(email_reg, text)