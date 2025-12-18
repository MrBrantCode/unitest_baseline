"""
QUESTION:
Create a function `isValidEmail` that checks if a given string is a valid email address. The function should return `True` if the string is a valid email and `False` otherwise. The email address should be in the standard format of local part followed by '@' and then the domain, and it should not contain any whitespace.
"""

import re

def isValidEmail(string):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    return bool(re.search(regex, string))