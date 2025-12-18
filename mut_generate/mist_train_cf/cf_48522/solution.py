"""
QUESTION:
Create a function `find_emails` that takes a text string and a top-level domain as input. The function should return a list of all email addresses in the text that end with the specified top-level domain. The email addresses should be in the format 'localpart@domain'. The localpart can contain alphanumeric characters, periods (.), underscores (_), percent signs (%), plus signs (+), and hyphens (-). The domain should match the specified top-level domain.
"""

import re

def find_emails(text, top_level_domain):
    """
    This function finds all email addresses in a text string that end with the specified top-level domain.

    Args:
        text (str): The text string where we want to find email addresses.
        top_level_domain (str): The common top-level domain.

    Returns:
        list: A list of all email addresses in the text that end with the specified top-level domain.
    """
    # Create a regex pattern for the emails
    pattern = r'\b[A-Za-z0-9._%+-]+@' + top_level_domain + r'\b'

    # Find matches
    return re.findall(pattern, text)