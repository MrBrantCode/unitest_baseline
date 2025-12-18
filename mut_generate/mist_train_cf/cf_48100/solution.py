"""
QUESTION:
Write a function `is_valid_phone_number` that takes a string `phone_number` as input and returns `True` if the string matches the format "XXX-XXX-XXXX" where X is a digit, and `False` otherwise. The function should reject strings that contain non-numeric and non-hyphen characters, as well as strings that do not match the exact format.
"""

import re

def is_valid_phone_number(phone_number):
    pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    return bool(pattern.match(phone_number))