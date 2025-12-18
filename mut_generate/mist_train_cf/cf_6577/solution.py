"""
QUESTION:
Design a function `extract_emails(html, spam_domain=None)` that takes an HTML string and an optional `spam_domain` parameter. The function should extract all unique, valid email addresses from the HTML string, excluding any emails from the specified `spam_domain` if provided. The extracted email addresses should be sorted in alphabetical order and returned as a list.
"""

import re

def extract_emails(html, spam_domain=None):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    emails = re.findall(pattern, html)
    validated_emails = [email for email in emails if re.match(pattern, email)]
    
    unique_emails = list(set(validated_emails))
    
    if spam_domain:
        filtered_emails = [email for email in unique_emails if not email.endswith(spam_domain)]
    else:
        filtered_emails = unique_emails
    
    return sorted(filtered_emails)