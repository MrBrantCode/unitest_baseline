"""
QUESTION:
Create a function `extract_asterisk_phrases` that takes a string `text` as input and returns a list of phrases enclosed between two asterisk (*) symbols. The function should use regular expressions to identify the phrases. The phrases should be returned without the enclosing asterisks.
"""

import re

def extract_asterisk_phrases(text):
    """
    Extracts phrases enclosed between two asterisk (*) symbols from a given text.

    Args:
    text (str): The input text to extract phrases from.

    Returns:
    list: A list of phrases enclosed between two asterisk symbols.
    """
    pattern = r'\*([^*]+)\*'
    return re.findall(pattern, text)