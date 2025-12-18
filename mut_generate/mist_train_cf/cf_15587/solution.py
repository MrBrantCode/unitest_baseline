"""
QUESTION:
Write a function `replace_key_with_value(s, key, value)` that takes a string `s`, a key, and a value as parameters. The function should replace all occurrences of the key with the value in the string, but only if the key is a separate word. The function should be case-insensitive and handle cases where the key has punctuation marks attached to it. The key and value should be replaced accordingly, regardless of case.
"""

import re

def replace_key_with_value(s, key, value):
    # Create a regular expression pattern to match the key as a separate word
    pattern = r'\b' + re.escape(key) + r'\b'
    # Replace all occurrences of the key with the value using the pattern
    new_s = re.sub(pattern, value, s, flags=re.IGNORECASE)
    return new_s