"""
QUESTION:
Create a function `find_able_words` that takes a string as input and returns a list of all words ending with "able" that are preceded by a digit and are not part of a larger word. The function should use a regular expression pattern to find the words.
"""

import re

def find_able_words(text):
    """
    This function finds all words ending with "able" that are preceded by a digit 
    and are not part of a larger word.

    Args:
        text (str): The input string to search for words.

    Returns:
        list: A list of words ending with "able" that meet the specified conditions.
    """
    pattern = r"(?<!\w)\d\w*able\b(?!\w)"
    return re.findall(pattern, text)