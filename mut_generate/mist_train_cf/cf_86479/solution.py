"""
QUESTION:
Create a function `replace_word` that takes a string and two parameters, `key` and `value`. The function should replace all occurrences of `key` in the string with `value`, but only if `key` is a separate word. The function should be case-insensitive and handle cases where `key` has punctuation marks attached to it. The function should also handle cases where `key` is a substring of a larger word, but not a separate word, and should not replace it in such cases.
"""

import re

def replace_word(string, key, value):
    """
    Replace all occurrences of key in the string with value, 
    but only if key is a separate word.

    Args:
        string (str): The input string.
        key (str): The word to be replaced.
        value (str): The replacement word.

    Returns:
        str: The modified string with key replaced by value.
    """
    # Create a regular expression pattern to match the key as a separate word
    pattern = r"\b" + re.escape(key) + r"\b"
    # Replace all occurrences of the key with the value using the pattern
    replaced_string = re.sub(pattern, value, string, flags=re.IGNORECASE)
    return replaced_string