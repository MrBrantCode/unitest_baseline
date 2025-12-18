"""
QUESTION:
Create a function `email_domain_checker` that checks the validity of an email address and determines its domain. The function should take a string as input and output 'Valid Email' along with the domain if the email is valid, and 'Invalid Email' otherwise. Assume the input is a string and does not support certain valid but less commonly used characters in email addresses.
"""

import re

def email_domain_checker(email):
    # regular expression to match email
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    
    if re.match(pattern, email):
        domain = email.split('@')[1]
        return 'Valid Email\nDomain: ' + domain
    else:
        return 'Invalid Email'