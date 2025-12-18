"""
QUESTION:
Implement a function `has_valid_emphasis` that takes a string `document` as input and returns `True` if the document contains one or more valid emphasis sequences, and `False` otherwise. A valid emphasis sequence is a sequence of one or two asterisks or underscores, followed by a non-whitespace character, followed by the same sequence of asterisks or underscores.
"""

import re

def has_valid_emphasis(document: str) -> bool:
    emphasis_pattern = r'(\*{1,2}|_{1,2})\S+\1'
    return bool(re.search(emphasis_pattern, document))