"""
QUESTION:
Create a function `is_valid_telephone_number` that takes a string as input and returns `True` if the string represents a valid American telephone number in the format (AAA) BBB-CCCC, where A, B, and C are digits from 0 to 9, and `False` otherwise.
"""

import re

def is_valid_telephone_number(number):
    match = re.fullmatch(r'\(\d{3}\) \d{3}-\d{4}', number)
    return match is not None