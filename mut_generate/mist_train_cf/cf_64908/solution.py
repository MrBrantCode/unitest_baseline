"""
QUESTION:
Extract Email Addresses from a String. 

Create a function named `extract_emails` that takes a string as input and returns a list of all email addresses present in the string. The email addresses can be in various formats and may have different domain names. The function should be able to handle a wide range of possible email formats, including those with alphanumeric characters, dots, underscores, pluses, and hyphens in both the local part and the domain.
"""

import re

def extract_emails(content):
    """
    Extracts all email addresses from a given string.

    Args:
        content (str): The string to extract email addresses from.

    Returns:
        list: A list of all email addresses found in the string.
    """
    email_regex = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(email_regex, content)