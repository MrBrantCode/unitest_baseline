"""
QUESTION:
Write a function named `remove_whitespace` that takes a string as input. The function should remove any leading and trailing special characters, remove any leading and trailing whitespaces, and replace multiple consecutive whitespace characters between words with a single space. The function should return the resulting string.
"""

import re

def remove_whitespace(s):
    s = re.sub(r'^[^a-zA-Z0-9]+|[^a-zA-Z0-9]+$', '', s)
    s = s.strip()
    s = re.sub(r'\s+', ' ', s)
    return s