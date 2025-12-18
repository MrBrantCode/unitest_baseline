"""
QUESTION:
Extract all email addresses from a given text using a regular expression in Python.

Create a function called `extract_email_addresses` that takes a string `text` as input and returns a list of all unique email addresses found in the text.

The regular expression pattern should match common email address formats, including alphanumeric characters, dots, underscores, percent signs, plus signs, hyphens, and top-level domains with at least two alphabetic characters.

Restrictions:
- Use the `re` module in Python to work with regular expressions.
- The function should return a list of unique email addresses found in the text.
- The email addresses should be extracted from the text in a case-sensitive manner.
"""

import re

def extract_email_addresses(text):
    """
    Extract all unique email addresses from a given text using a regular expression.

    Args:
        text (str): The input text to search for email addresses.

    Returns:
        list: A list of unique email addresses found in the text.
    """
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    matches = re.findall(pattern, text)
    return list(set(matches))  # Return unique email addresses