"""
QUESTION:
Design a function named `replace_emails` that takes a string as input and returns a new string where all email addresses are replaced with the string "EMAIL". The function should use regular expressions to match and substitute email addresses. The matched email addresses should be in the format of local-part@domain, where local-part can contain alphanumeric characters, dot, underscore, percent, plus, or minus, domain can contain alphanumeric characters, dot, or dash, and the top-level domain should be at least two alphabetic characters. The function should match whole email addresses only, excluding partial matches within other words.
"""

import re

def replace_emails(text):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    result = re.sub(email_regex, 'EMAIL', text)
    return result