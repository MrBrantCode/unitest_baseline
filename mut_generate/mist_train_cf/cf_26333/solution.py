"""
QUESTION:
Create a function `validate_phone_number` that takes a string as input and returns `True` if it matches the US phone number format, otherwise returns `False`. The US phone number format can include an optional country code, area code, and extension, and can be separated by dots, hyphens, or spaces.
"""

import re

def validate_phone_number(phone_number):
    pattern = r'^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$'
    return bool(re.match(pattern, phone_number))