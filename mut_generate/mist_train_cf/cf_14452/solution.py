"""
QUESTION:
Create a function `telephone_number_matcher` that takes a string as input and returns `True` if the string matches the specified telephone number format, and `False` otherwise. The format consists of three digits for the area code, followed by a hyphen, followed by a seven-digit phone number.
"""

import re

def telephone_number_matcher(s):
    pattern = r'^\d{3}-\d{7}$'
    return bool(re.match(pattern, s))