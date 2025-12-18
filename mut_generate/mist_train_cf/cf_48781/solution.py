"""
QUESTION:
Create a function `highlight_semicolon_sequences(text)` that takes a string `text` as input and returns all sequences of characters that contain a semi-colon symbol ";". The function should use regular expressions to match any sequence of characters before and after a semi-colon.
"""

import re

def highlight_semicolon_sequences(text):
    pattern = re.compile(r'.+;.+')
    matches = pattern.findall(text)
    return matches