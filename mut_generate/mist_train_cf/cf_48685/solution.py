"""
QUESTION:
Create a function `valid_email(email, domain_list)` that checks if a given email address is valid and its domain is in a predefined list of reputable domains. The function should return `True` if the email is valid and its domain is in the list, `False` otherwise. The function should use a regular expression pattern to validate the basic syntax of the email address.
"""

import re

def validate_email(email, domain_list):
    email_pattern = "^[\w\.-]+@[\w\.-]+(\.[\w]+)+$"
    if re.match(email_pattern, email):
        domain = email.split('@')[-1]
        return domain in domain_list
    return False