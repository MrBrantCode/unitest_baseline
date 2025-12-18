"""
QUESTION:
Create a function `verify_email` that takes an email address as input and returns `True` if the email address is valid, and `False` along with an error message if it's not. The function should use regular expressions to verify the email format (Name@Domain.TLD) and check if the domain is in a predefined list of acceptable domains (`["gmail.com", "yahoo.com", "hotmail.com"]`).
"""

import re

def verify_email(email):
    acceptable_domains = ["gmail.com", "yahoo.com", "hotmail.com"]
    pattern = r"[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
    
    if re.match(pattern, email):
        domain = email.split('@')[1] 
        if domain in acceptable_domains:
            return True
        else:
            return False, "The email domain is not acceptable."
    else:
        return False, "The email format does not match."