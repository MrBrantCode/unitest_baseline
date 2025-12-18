"""
QUESTION:
Write a function called `validate_email(email)` that checks whether an email address is in the correct format. The function should return `True` if the email address is valid and `False` otherwise. Assume a basic email format consisting of alphanumeric characters, dots, underscores, and a single '@' symbol separating the local part from the domain, with a top-level domain consisting of 2-3 characters.
"""

import re

def validate_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,email)):  
        return True  
    else:  
        return False