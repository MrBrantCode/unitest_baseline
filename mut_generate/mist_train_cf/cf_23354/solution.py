"""
QUESTION:
Create a function `extract_emails` that takes a string as input and returns a list of all email addresses found in the string. The function should be able to extract email addresses in the format of "local-part@domain" where the local-part can contain alphanumeric characters and special characters ".+-_", the domain can contain alphanumeric characters and hyphen, and the domain extension can contain alphanumeric characters, hyphen, and dot.
"""

import re

def extract_emails(string):
    """
    This function takes a string as input and returns a list of all email addresses found in the string.
    
    Args:
        string (str): The input string that may contain email addresses.
    
    Returns:
        list: A list of email addresses found in the string.
    """
    return re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", string)