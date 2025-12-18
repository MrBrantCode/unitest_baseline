"""
QUESTION:
Create a function named `validate_email` that takes a string `email` as input and returns "Valid Email" if the email is valid and "Invalid Email" otherwise. The function should use a regular expression to validate the email format, which should adhere to common formatting rules for email addresses. The regular expression should consider an email valid if it starts with alphanumeric characters, possibly followed by a dot or an underscore, then another sequence of alphanumeric characters, an at symbol, another sequence of alphanumeric characters, a dot, and finally 2 or 3 alphanumeric characters.
"""

import re

def validate_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,email)):  
        return "Valid Email"
    else:  
        return "Invalid Email"