"""
QUESTION:
Write a function named `verify_string` that takes a string as input. The function should return `True` if the input string starts with a Unicode character from the range 0370-03FF (Greek and Coptic block), followed by exactly 3 characters that are either lower case vowels or consonants in any order, and then a sequence of at least 2 but not more than 4 prime number digits (2, 3, 5, or 7). The function should ignore any leading or trailing white spaces and return `False` otherwise.
"""

import re

def verify_string(s):
    pattern = r'\A[^\S]*[\u0370-\u03FF][a-z]{3}[2357]{2,4}[^\S]*\Z'
    match = re.fullmatch(pattern, s)
    return bool(match)