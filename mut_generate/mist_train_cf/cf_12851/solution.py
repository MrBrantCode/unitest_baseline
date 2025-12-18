"""
QUESTION:
Create a regular expression to extract email addresses from a given list of text. The email addresses can be followed by punctuation marks or special characters. The regular expression should match the standard email format, where the username part can contain letters, digits, dots, underscores, percent signs, plus and minus signs, and the domain part can contain letters, digits, dots, and hyphens, with the domain extension having at least two letters.
"""

import re

def extract_emails(text):
    """
    Extract email addresses from a given text.

    The email addresses can be followed by punctuation marks or special characters.
    The regular expression matches the standard email format, where the username part 
    can contain letters, digits, dots, underscores, percent signs, plus and minus signs, 
    and the domain part can contain letters, digits, dots, and hyphens, with the domain 
    extension having at least two letters.

    Args:
        text (str): The text to extract email addresses from.

    Returns:
        list: A list of extracted email addresses.
    """
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    return re.findall(email_regex, text)