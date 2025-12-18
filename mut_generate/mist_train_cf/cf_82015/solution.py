"""
QUESTION:
Create a function named `find_specific_sequences` that takes a string `text` as input and returns a list of all sequences of characters that start with "pr" and end with "oo" (case-insensitive), with no restrictions on the characters in between. The function should use regular expressions and be optimized for handling large inputs.
"""

import re

def find_specific_sequences(text):
    pattern = re.compile(r'\bpr\w*oo\b', re.IGNORECASE)
    return pattern.findall(text)