"""
QUESTION:
Create a function named `is_exclusive_alphabet` that takes a string as input and returns `True` if the string exclusively consists of alphabetic characters ranging from "a" to "z" (both uppercase and lowercase) and `False` otherwise. The function should not allow any other symbols or digits in the string.
"""

import re

def is_exclusive_alphabet(string):
    match = re.fullmatch('[A-Za-z]*', string)
    return match is not None