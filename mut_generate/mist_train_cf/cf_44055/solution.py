"""
QUESTION:
Develop a function named `replace_urls_with_term` that takes a string as input and returns a string with all URLs replaced with the term "URL". The function should use regular expressions to match both http and https URLs.
"""

import re

def replace_urls_with_term(string: str) -> str:
    return re.sub(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
        'URL', string)