"""
QUESTION:
Create a function named `extract_emails(text)` that extracts all existing email addresses from a given text. The function should be able to handle varying email address formats and domain variations. The input is a string `text`, and the output should be a list of extracted email addresses.
"""

import re

def extract_emails(text):
    email_regex_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    return re.findall(email_regex_pattern, text)