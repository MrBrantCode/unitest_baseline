"""
QUESTION:
Create a function called `find_emails` that takes a string `text` as input and returns a list of all email addresses found in the text. The function should be able to identify email addresses with the general format `localpart@domain`, where `localpart` and `domain` can contain alphanumeric characters, periods, and hyphens.
"""

import re

def find_emails(text):
    pattern = r'[\w\.-]+@[\w\.-]+'
    return re.findall(pattern, text)