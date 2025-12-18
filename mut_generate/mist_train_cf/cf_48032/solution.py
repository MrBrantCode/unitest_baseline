"""
QUESTION:
Create a function `check_mutual_palindromes(s1, s2)` that checks if two input strings are mutual palindromes. The function should disregard punctuation marks, spaces, and case sensitivity. It should return `True` if both strings are palindromes, and `False` otherwise.
"""

import re

def check_mutual_palindromes(s1, s2):
    # Remove punctuation marks & convert to lower case
    s1 = re.sub(r'[\W_]', '', s1.lower())
    s2 = re.sub(r'[\W_]', '', s2.lower())

    # Check if they are both palindromes
    return s1 == s1[::-1] and s2 == s2[::-1]