"""
QUESTION:
Create a function `classify_syntactic_units` that takes a string `text` as input and returns all substrings that consist entirely of lowercase letters and are at least 5 characters long.
"""

import re

def classify_syntactic_units(text):
    regex = r"[a-z]{5,}"
    matches = re.findall(regex, text)
    return matches