"""
QUESTION:
Write a function `match_alphabet_only` that takes a string as input and returns `True` if the string contains only alphabetical characters (both lowercase and uppercase) and `False` otherwise. The function should use regular expressions to achieve this.
"""

import re

def match_alphabet_only(text):
    pattern = "^[a-zA-Z]*$"
    return bool(re.fullmatch(pattern, text))