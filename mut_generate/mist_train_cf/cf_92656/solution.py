"""
QUESTION:
Create a function `validate_email` that takes a string as input and returns a list of valid email addresses that do not contain the domain "gmail.com". Use regular expressions to match valid email addresses.
"""

import re

def validate_email(text):
    """
    Returns a list of valid email addresses that do not contain the domain "gmail.com".
    
    Args:
    text (str): A string containing one or more email addresses.
    
    Returns:
    list: A list of valid email addresses that do not contain the domain "gmail.com".
    """
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, text)
    return [email for email in emails if '@gmail.com' not in email]