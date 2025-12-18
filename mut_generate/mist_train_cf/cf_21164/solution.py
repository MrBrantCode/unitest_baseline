"""
QUESTION:
Design a function named `extract_emails(html)` that takes a string of HTML as input. The function should use regular expressions to extract email addresses from the HTML, filter out any duplicate addresses, and return a list of unique email addresses sorted in alphabetical order.
"""

import re

def extract_emails(html):
    # Extract email addresses using regular expressions
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, html)

    # Remove duplicate email addresses and sort in alphabetical order
    return sorted(set(emails))