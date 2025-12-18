"""
QUESTION:
Design a function `extract_emails(html)` that extracts and validates email addresses from a given HTML string. The function should use regular expressions to match email addresses in the format specified by the RFC 5322 standard. The function should return a list of valid email addresses found in the HTML string.
"""

import re

def extract_emails(html):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_regex, html)
    
    # Validate emails using RFC 5322 standard
    valid_emails = []
    for email in emails:
        if re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$', email):
            valid_emails.append(email)
    
    return valid_emails