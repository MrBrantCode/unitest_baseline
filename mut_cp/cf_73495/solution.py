"""
ORIGINAL QUESTION:
Create a function `check_string(s)` that returns `True` if the given string `s` contains a word that starts with the letter "a", contains at least one digit, and ends with a non-alphanumeric character, and `False` otherwise. The function should match the word as a whole, not as part of a longer word.
"""

import re

def check_string(s):
    pattern = r"\ba.*\d.*\W\b"
    if re.search(pattern, s):
        return True
    else:
        return False