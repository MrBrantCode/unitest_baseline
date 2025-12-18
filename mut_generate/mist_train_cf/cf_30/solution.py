"""
QUESTION:
Write a function `extract_emails` that takes a string as input and returns a list of unique email addresses found in the string. The function should be able to handle various formats of email addresses, including those with different domains and subdomains, and should correctly handle edge cases such as email addresses preceded or followed by punctuation marks or special characters, and email addresses containing non-alphanumeric characters.
"""

import re

def extract_emails(string):
    # Use regular expression pattern to find all email addresses in the string
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    matches = re.findall(pattern, string)
    
    # Remove any duplicate email addresses
    unique_emails = list(set(matches))
    
    return unique_emails