"""
QUESTION:
Replace all occurrences of the word "the" with "a" in a given string while preserving the original word order and case, and ignoring any occurrences of "the" that are part of another word. The function should be named `replace_the_with_a` and it should take a string as input and return the modified string.
"""

import re

def replace_the_with_a(word_string):
    """
    Replaces all occurrences of 'the' with 'a' in a given string, 
    preserving the original word order and case, and ignoring any 
    occurrences of 'the' that are part of another word.

    Args:
        word_string (str): The input string.

    Returns:
        str: The modified string with all 'the' replaced with 'a'.
    """

    # Create a regular expression pattern that matches "the" as a whole word
    pattern = r'\bthe\b'

    # Use the sub() function to replace all occurrences of the pattern with "a"
    new_word_string = re.sub(pattern, 'a', word_string, flags=re.IGNORECASE)

    return new_word_string