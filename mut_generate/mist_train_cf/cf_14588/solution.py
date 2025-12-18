"""
QUESTION:
Write a function named `replace_language` that takes a string `text` as input and returns the string with all occurrences of 'Python' replaced with 'Java' only when 'Python' is a standalone word, not part of a larger word.
"""

import re

def replace_language(text):
    return re.sub(r'\bPython\b', 'Java', text)