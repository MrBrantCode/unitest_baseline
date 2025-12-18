"""
QUESTION:
Create a function `find_com_email_addresses` that takes a string `text` as input and returns all the email addresses that end with '.com'. The function should use regular expressions to find the email addresses.
"""

import re

def find_com_email_addresses(text):
    """
    This function finds all .com emails from the given text
    """
    email_regex = r'[a-zA-Z0-9+_\-\.]+@[0-9a-zA-Z][.-0-9a-zA-Z]*.com'
    return re.findall(email_regex, text)