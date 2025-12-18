"""
QUESTION:
Write a function `replace_key_with_value(s, key, value)` that takes a string `s`, a key, and a value as parameters and replaces all occurrences of the key with the value in the string. The function should only replace the key if it is a separate word and handle cases where the key is capitalized or has punctuation marks attached to it. The replacement should be case-insensitive.
"""

import re

def replace_key_with_value(s, key, value):
    # Create a regular expression pattern to match the key as a separate word
    pattern = r'\b' + re.escape(key) + r'\b'
    # Replace all occurrences of the key with the value using the pattern
    new_s = re.sub(pattern, value, s, flags=re.IGNORECASE)
    return new_s