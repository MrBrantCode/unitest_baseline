"""
QUESTION:
Create a function named `find_phoenix` that takes a string `text` as input and returns a message indicating whether the word "phoenix" (case-insensitive) appears at the start of any paragraph within the text. The function should consider each line as a separate paragraph and ignore case differences.
"""

import re

def find_phoenix(text):
    pattern = re.compile(r'^phoenix', re.IGNORECASE | re.MULTILINE)
    matches = pattern.findall(text)
    
    if matches:
        return 'The lexeme "phoenix" is found at the inception of a paragraph.'
    else:
        return 'The lexeme "phoenix" is NOT found at the inception of a paragraph.'