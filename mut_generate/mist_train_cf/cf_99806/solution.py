"""
QUESTION:
Extract Emails Function
Write a function that takes a text string as input and returns a list of all email addresses found in the text. The email addresses should be in the standard format (e.g., username@example.com). The function should return all matches found in the text.
"""

import re

def extract_emails(text):
    """
    Extracts email addresses from a given text.

    Args:
        text (str): The input text to search for email addresses.

    Returns:
        list: A list of email addresses found in the text.
    """
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)