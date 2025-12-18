"""
QUESTION:
Create a function, validate_consecutive_numbers, that takes a string as input and returns True if the string contains exactly 5 consecutive digits, and False otherwise. The input string can contain other characters, but the function should return True only if it contains 5 consecutive digits.
"""

import re

def validate_consecutive_numbers(s):
    return bool(re.search(r'\d{5}', s))