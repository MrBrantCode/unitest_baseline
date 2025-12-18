"""
QUESTION:
Create a function `is_example_com_email(email)` that takes an email address as input and returns `True` if the email is associated with the domain "example.com" and `False` otherwise. The function should allow for common email username characters (alphanumeric, dot, underscore, plus, minus) but not match subdomains of example.com.
"""

import re

def is_example_com_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@example\.com$"
    if re.search(pattern, email):
        return True
    return False