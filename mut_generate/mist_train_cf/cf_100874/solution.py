"""
QUESTION:
Create a function `parse_text` that takes a string as input and returns the text between the "%" symbol and either a whitespace or a colon. The input string can have zero or one whitespace character after the "%" symbol. The function should return the text in a case where the "%" symbol is immediately followed by the desired text, as well as in a case where there is a single whitespace character between the "%" symbol and the desired text.
"""

import re

def parse_text(text):
    match = re.search(r'%[\s]?([a-zA-Z]+)[\s:]', text)
    if match:
        return match.group(1)