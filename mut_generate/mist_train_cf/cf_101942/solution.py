"""
QUESTION:
Write a function `convert_string` that takes a string as input, converts it to lowercase, removes punctuation marks and digits, and preserves whitespace characters.
"""

import string

def convert_string(s):
    """Converts a string to lowercase, removes punctuation marks and digits, and preserves whitespace characters."""
    return ''.join(filter(lambda x: not x.isdigit(), s.lower().translate(str.maketrans("", "", string.punctuation))))