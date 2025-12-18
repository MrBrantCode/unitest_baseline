"""
QUESTION:
Create a function `find_phoenix_at_paragraph_start` that takes a string `text` as input and returns a boolean indicating whether the word "phoenix" (case-insensitive) appears at the start of a paragraph in the given text. The function should treat each line as a separate string. 

The function should use a regular expression pattern to match the word "phoenix" at the start of a string. The pattern should be case-insensitive.
"""

import re

def find_phoenix_at_paragraph_start(text):
    pattern = r'^phoenix'
    matches = re.match(pattern, text, re.IGNORECASE)
    return bool(matches)