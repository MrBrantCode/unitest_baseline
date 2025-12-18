"""
QUESTION:
Create a function called `filter_emails` that takes a list of email addresses as input and returns a new list containing only the email addresses with the domain name "example.com". Use a regular expression to match the domain name. The function should be case-sensitive and only match emails with the exact domain name "example.com".
"""

import re

def filter_emails(emails):
    pattern = r"[a-zA-Z0-9_.+-]+@example\.com"
    return [email for email in emails if re.match(pattern, email)]