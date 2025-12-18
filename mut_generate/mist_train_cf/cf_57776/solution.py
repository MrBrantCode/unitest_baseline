"""
QUESTION:
Create a function named `count_emails_in_text` that takes a string `text` as input and returns a dictionary containing the count of each unique email address found in the text. The function should consider email addresses case-insensitive, handle multiple email addresses on the same line, and punctuation immediately following an email address. The regular expression used should follow common email formatting standards, including a local part, the @ symbol, a domain part, and a top-level domain part.
"""

import re
from collections import Counter

def count_emails_in_text(text):
    # Extract all email addresses using regex pattern
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    found_emails = re.findall(email_pattern, text, re.IGNORECASE)
    
    # Convert all emails to lowercase to ensure case-insensitivity
    found_emails = [email.lower() for email in found_emails]
    
    # Maintain a count of each unique email address
    email_counts = Counter(found_emails)
    
    return email_counts