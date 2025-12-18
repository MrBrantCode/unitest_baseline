"""
QUESTION:
Write a function `detect_phone_number` that takes a string as input and returns True if the string matches the pattern of a phone number with a country code, False otherwise. The phone number pattern should start with a plus sign (+) followed by a two-digit country code (between 1 and 99), a hyphen (-), and then a 10-digit phone number.
"""

import re

def detect_phone_number(phone_number):
    pattern = r'^\+[1-9][0-9]-\d{10}$'
    return bool(re.match(pattern, phone_number))