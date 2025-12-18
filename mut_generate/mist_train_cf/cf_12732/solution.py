"""
QUESTION:
Construct a regular expression pattern for a function called `word_format_pattern` that matches a single word in the format "XX-XXX-XXX". The word must meet the following criteria: 
- The first two characters are uppercase letters.
- The next three characters are lowercase letters.
- The last three characters are a mix of uppercase and lowercase letters.
- No digits or special characters are allowed.
"""

import re

def word_format_pattern(word):
    """
    Check if the word matches the pattern "XX-XXX-XXX" where:
    - The first two characters are uppercase letters.
    - The next three characters are lowercase letters.
    - The last three characters are a mix of uppercase and lowercase letters.
    - No digits or special characters are allowed.

    Args:
        word (str): The input word to be checked.

    Returns:
        bool: True if the word matches the pattern, False otherwise.
    """
    pattern = r"^[A-Z]{2}-[a-z]{3}-[a-zA-Z]{3}$"
    return bool(re.match(pattern, word))