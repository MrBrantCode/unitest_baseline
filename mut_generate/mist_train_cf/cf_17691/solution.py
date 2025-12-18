"""
QUESTION:
Create a function `searchFooBar` that constructs a regular expression to search for all words. The words must start with 'Foo', followed by zero or more word characters, and end with 'Bar'. The search should be case-insensitive, allowing any combination of uppercase and lowercase letters.
"""

import re

def searchFooBar(s):
    """
    Searches for words that start with 'Foo', followed by zero or more word characters, and end with 'Bar' in any combination of uppercase and lowercase letters.

    Args:
        s (str): The input string to search.

    Returns:
        list: A list of words that match the pattern.
    """
    pattern = r'\b[Ff][Oo]{2}\w*[Bb][Aa][Rr]\b'
    return re.findall(pattern, s, re.IGNORECASE)