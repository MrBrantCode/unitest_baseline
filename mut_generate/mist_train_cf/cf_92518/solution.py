"""
QUESTION:
Write a regular expression to extract email addresses from a given text. The email extraction function, named `extract_emails`, should take a list of strings as input and return a list of extracted email addresses. The regular expression should handle cases where emails are followed by punctuation marks or other special characters. The extracted email addresses should follow the standard format where the username part can contain letters, digits, dots, underscores, percent signs, plus signs, and minus signs. The domain part should contain letters, digits, dots, and hyphens, and the domain extension should have at least two letters.
"""

import re

def extract_emails(text_list):
    """
    Extracts email addresses from a list of strings.

    Args:
        text_list (list): A list of strings.

    Returns:
        list: A list of extracted email addresses.
    """
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    emails = [match for text in text_list for match in re.findall(email_regex, text)]
    return emails