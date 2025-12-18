"""
QUESTION:
Construct a regular expression pattern that matches any string containing an email address, excluding emails with the domain "gmail.com". The pattern should validate the entire string, not just a substring.
"""

import re

def find_emails(text):
    """
    Find all email addresses in the given text, excluding those with the domain "gmail.com".

    Args:
    text (str): The input text to search for email addresses.

    Returns:
    list: A list of email addresses without the domain "gmail.com".
    """
    pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    emails = re.findall(pattern, text)
    return [email for email in emails if 'gmail.com' not in email]