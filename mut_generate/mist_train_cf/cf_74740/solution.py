"""
QUESTION:
Create a function called `email_validation` that takes an email address as input and returns a string indicating whether the email is valid or not. The function should only accept email addresses with ".edu" or ".org" domains.
"""

import re

def email_validation(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.(edu|org)$"
    
    if re.match(pattern, email):
        return "Email is valid"
    else:
        return "Email is invalid"