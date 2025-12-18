"""
QUESTION:
Write a function called `sort_emails` that takes a list of email addresses as input, removes any invalid email addresses, and returns the remaining valid email addresses sorted by their character count. An email address is considered valid if it matches the regular expression for email validation.
"""

import re

def sort_emails(emails):
    email_regex = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
    valid_emails = [email for email in emails if re.match(email_regex, email) is not None]
    valid_emails.sort(key=len)
    return valid_emails