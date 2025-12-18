"""
QUESTION:
Write a function `match_sentence` that takes a sentence as input and returns `True` if the sentence starts with a capital letter, contains the word "dog" followed by any number of characters except "x" and "y", and ends with either a full-stop, exclamation mark, or question mark. The function should be case-sensitive and should not match "dog" written in capital letters.
"""

import re

def match_sentence(sentence):
    pattern = r"^[A-Z][^xy]*dog[^xy]*[.!?]$"
    return bool(re.match(pattern, sentence))