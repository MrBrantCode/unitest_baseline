"""
QUESTION:
Write a function `to_snake_case` that converts a given string into snake_case by replacing spaces and punctuation with underscores and making all characters lowercase. The function should be efficient for large strings and use regular expressions to remove punctuation.
"""

import re

def to_snake_case(txt):
    txt_without_punctuation = re.sub(r'\W+', '_', txt)
    return txt_without_punctuation.lower()