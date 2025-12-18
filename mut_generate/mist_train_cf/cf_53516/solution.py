"""
QUESTION:
Create a function named `is_alphabet_string` that takes one string parameter and returns `True` if the string exclusively consists of one or more lowercase alphabetic characters from "a" to "z" and `False` otherwise.
"""

import re

def is_alphabet_string(s):
    if(re.search('^[a-z]+$',s)):
        return True
    else:
        return False