"""
QUESTION:
Write a Python function called `extract_emails` that uses regular expressions to extract all the email addresses from a given text. The function should take a string `text` as an argument and return a list of extracted email addresses. The email extraction should consider common email address formats, including letters (both capital and lowercase), digits, and special characters.
"""

import re

def extract_emails(text):
    email_regex = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    return re.findall(email_regex, text)