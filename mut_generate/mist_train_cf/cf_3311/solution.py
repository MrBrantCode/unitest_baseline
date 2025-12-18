"""
QUESTION:
Write a function called `replace_the_with_a` that takes a string of words as input and returns a new string where all occurrences of the word "the" are replaced with "a", while preserving the original word order and case, and ignoring any occurrences of the word "the" that are part of another word.
"""

import re

def replace_the_with_a(word_string):
    """
    Replaces all occurrences of the word "the" with "a" in a given string,
    preserving the original word order and case, and ignoring any occurrences
    of the word "the" that are part of another word.

    Args:
        word_string (str): The input string.

    Returns:
        str: The modified string with all "the" replaced with "a".
    """

    # Create a regular expression pattern that matches "the" as a whole word
    pattern = r'\bthe\b'

    # Use the sub() function to replace all occurrences of the pattern with "a"
    return re.sub(pattern, 'a', word_string, flags=re.IGNORECASE)