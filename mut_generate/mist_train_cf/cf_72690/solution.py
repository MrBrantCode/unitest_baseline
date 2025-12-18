"""
QUESTION:
Write a function called `find_emails` that takes a string `text` as input and returns all unique valid email addresses in the text that comply with the RFC 5322 standard. The function should use regular expressions to filter out invalid email addresses. The email addresses can be located anywhere in the text and may be surrounded by other characters or punctuation.
"""

import re

def find_emails(text):
    """
    This function takes a string text as input and returns all unique valid email addresses in the text 
    that comply with the RFC 5322 standard.

    Args:
        text (str): A string containing email addresses.

    Returns:
        list: A list of valid email addresses.
    """
    pattern = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
    return set(re.findall(pattern, text))