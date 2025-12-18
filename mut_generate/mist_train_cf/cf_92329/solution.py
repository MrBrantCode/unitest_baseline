"""
QUESTION:
Create a function `extract_sion_words` that takes a string `paragraph` as input, extracts all words that end with 'sion' and are preceded and followed by a space or punctuation mark, and returns the extracted words in a list, sorted in alphabetical order. The function should be case-insensitive and support paragraphs of up to 500 words.
"""

import re

def extract_sion_words(paragraph):
    """
    Extracts all words that end with 'sion' from a given paragraph, 
    preceded and followed by a space or punctuation mark, and returns 
    the extracted words in a list, sorted in alphabetical order. The 
    function is case-insensitive.

    Args:
        paragraph (str): A string representing the paragraph of text.

    Returns:
        list: A list of words that end with 'sion', sorted in alphabetical order.
    """
    matches = re.findall(r'\b[A-Za-z]+sion\b', paragraph, re.IGNORECASE)
    return sorted(matches)