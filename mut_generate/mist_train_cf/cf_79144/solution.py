"""
QUESTION:
Write a function `match_phone_number(phone_number)` that takes a string as input and returns `True` if the string matches the following pattern, and `False` otherwise: 
The string starts with a plus sign followed by one to three digits (the country code), then a 6, and then exactly 10 more digits.
"""

import re

def match_phone_number(phone_number):
    pattern = r'\+\d{1,3}6\d{10}$'
    return bool(re.match(pattern, phone_number))