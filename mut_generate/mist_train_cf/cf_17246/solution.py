"""
QUESTION:
Create a function `extract_email_addresses` that takes a string `text` as input. The function should return a list of email addresses found in the text, where the email addresses are surrounded by whitespace or punctuation marks. The function should ignore email addresses with special characters such as !, ?, or -, and should only consider email addresses with domain names having at least two parts (e.g. example.com). The function should also exclude any leading or trailing whitespace or punctuation marks from the extracted email addresses.
"""

import re

def extract_email_addresses(text):
    """
    Extracts email addresses from a given text.

    The function returns a list of email addresses found in the text, where the email addresses are surrounded by 
    whitespace or punctuation marks. The function ignores email addresses with special characters such as !, ?, or -, 
    and only considers email addresses with domain names having at least two parts (e.g., example.com).

    Parameters:
    text (str): The text to extract email addresses from.

    Returns:
    list: A list of extracted email addresses.
    """
    
    pattern = r'\b(?<![!?\w-])[A-Za-z0-9]+(?:[._-][A-Za-z0-9]+)*@[A-Za-z0-9]+(?:[.-][A-Za-z0-9]+)*\.[A-Za-z]{2,}\b'
    return re.findall(pattern, text)