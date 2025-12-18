"""
QUESTION:
Write a function called `is_lower_case_alphabet_only` that takes a string as input and returns True if the string consists only of lowercase alphabetic characters from 'a' to 'z' and False otherwise.
"""

import re

def is_lower_case_alphabet_only(string):
    pattern = r'^[a-z]*$'
    if re.match(pattern, string):
        return True
    else:
        return False