"""
QUESTION:
Write a function named `replace_word` that takes a string, a key, and a value as parameters. It should replace all occurrences of the key with the value in the string only if the key is a separate word, handling cases where the key is capitalized or has punctuation marks attached to it. The function should be case-insensitive and not replace the key if it is a substring of a larger word.
"""

import re

def replace_word(string, key, value):
    pattern = r"\b" + re.escape(key) + r"\b"
    replaced_string = re.sub(pattern, value, string, flags=re.IGNORECASE)
    return replaced_string