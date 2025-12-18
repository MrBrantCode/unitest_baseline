"""
QUESTION:
Write a function named `check_string` that takes a string as input and returns `True` if the string consists of a hexadecimal number immediately followed by a small-cased vowel from the English alphabet, and `False` otherwise. The function should not match strings with whitespace or any characters between the hexadecimal number and the vowel.
"""

import re

def check_string(string):
    pattern = r'^[0-9A-Fa-f]+[aeiou]$'
    return bool(re.search(pattern, string))