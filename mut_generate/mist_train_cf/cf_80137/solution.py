"""
QUESTION:
Create a function `is_example_com_email(email)` that takes an email address as input and returns `True` if the email is associated with the domain 'example.com', and `False` otherwise. The function should use a regular expression to match the email addresses.
"""

import re

def is_example_com_email(email):
    """
    This function checks whether the input email is intrinsically linked with the domain example.com
    """
    # constructing the regular expression pattern
    pattern = r"[a-zA-Z0-9_.+-]+@example\.com$"
    
    # searching the pattern
    if re.search(pattern, email):
        return True
    else:
        return False