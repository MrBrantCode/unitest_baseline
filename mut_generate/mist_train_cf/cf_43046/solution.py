"""
QUESTION:
Implement the `validate_email` function to validate a given email address. The function should take an email address as input and return True if the email address is valid, and False otherwise. An email address is considered valid if it meets the following criteria: 
- It contains a single "@" symbol.
- The "@" symbol is not at the beginning or end of the email address.
- The part before the "@" symbol contains only alphanumeric characters, dots, hyphens, and underscores.
- The part after the "@" symbol contains only alphanumeric characters and dots.
- The email address ends with a valid top-level domain (e.g., .com, .org, .net).
"""

def validate_email(email):
    if email.count('@') != 1:  
        return False

    username, domain = email.split('@')  
    if not username or not domain:  
        return False

    if not username.replace('.', '').replace('-', '').replace('_', '').isalnum():  
        return False

    if not domain.replace('.', '').isalnum():  
        return False

    if not domain.endswith(('.com', '.org', '.net')):  
        return False

    return True 