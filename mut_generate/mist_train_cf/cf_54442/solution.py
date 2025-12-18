"""
QUESTION:
Create a function called `extract_emails` that uses regular expression to extract email addresses from a given string. The function should be able to handle common email formats and variations. The input string is considered to be obtained from an XML document and may contain non-email characters and invalid email addresses.
"""

import re

def extract_emails(xml_str):
    """
    Extracts email addresses from a given string using regular expressions.

    Args:
        xml_str (str): Input string containing email addresses.

    Returns:
        list: A list of extracted email addresses.
    """
    pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
    return re.findall(pattern, xml_str)