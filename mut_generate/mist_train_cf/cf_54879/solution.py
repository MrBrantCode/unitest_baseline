"""
QUESTION:
Write a function `anonymize_emails` that takes a string `text` as input and returns the text with all email addresses replaced with the string "EMAIL". The function should use regular expressions to identify email addresses. The regular expression should match common email address formats, including alphanumeric characters, periods, plus signs, and underscores before the '@' symbol, and alphanumeric characters, periods, and hyphens after the '@' symbol.
"""

import re

def anonymize_emails(text):
    # Email Regular Expression
    email_regex = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    
    # Substituting Emails
    anonymized_text = re.sub(email_regex, 'EMAIL', text)
    
    return anonymized_text