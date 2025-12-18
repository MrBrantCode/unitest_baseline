"""
QUESTION:
Create a function `validate_phone_number(input_number)` that checks if the given string adheres to the US telephone number format (XXX) XXX-XXXX, where X denotes any digit from 0-9. The function should return `True` if the input string matches the format and `False` otherwise.
"""

import re

def validate_phone_number(input_number):
    pattern = re.compile(r'\(\d{3}\) \d{3}-\d{4}')
    return bool(pattern.fullmatch(input_number))