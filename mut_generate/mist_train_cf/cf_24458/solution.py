"""
QUESTION:
Write a regular expression function `email_regex` that takes a string as input and returns a list of all email addresses found in the string. The email address should start with alphanumeric characters or special characters (dot, underscore, plus, hyphen), followed by '@', then alphanumeric characters or hyphen, then a dot, and finally alphanumeric characters or hyphen.
"""

import re

def email_regex(string):
    """
    This function takes a string as input and returns a list of all email addresses found in the string.
    
    Args:
        string (str): The input string to search for email addresses.
    
    Returns:
        list: A list of email addresses found in the string.
    """
    regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    return re.findall(regex, string)