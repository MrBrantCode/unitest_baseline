"""
QUESTION:
Create a function `validate_email_addresses` that takes a list of email addresses as input and returns a dictionary where the keys are the email addresses and the values are boolean indicators of their validity. The function should use a regular expression pattern that strictly follows standard email format rules, including the presence of an @ symbol, a domain name, and a top-level domain. The function should be able to handle edge cases such as uppercase letters in the domain name, multiple @ symbols, and special characters in the domain name, and it should have a time complexity of O(n), where n is the number of email addresses in the input list.
"""

import re

def validate_email_addresses(email_addresses):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    valid_emails = {}
    
    for email in email_addresses:
        is_valid = re.match(pattern, email) is not None
        valid_emails[email] = is_valid
    
    return valid_emails