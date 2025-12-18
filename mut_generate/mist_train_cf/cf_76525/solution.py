"""
QUESTION:
Create a function called `detect_ILike_sentences` that takes a string `text` as input. The function should return `True` if the input string is a sentence that starts with "I like" (ignoring case), and `False` otherwise.
"""

import re

def detect_ILike_sentences(text):
    pattern = re.compile(r'^(I like\b.*)', re.IGNORECASE)
    result = pattern.match(text)
    return result is not None