"""
QUESTION:
Create a function called `validate_phone_number` to validate a phone number. The function should take a phone number as input and return True if the phone number is valid and False otherwise. A valid phone number consists of exactly 10 digits. The function should use regular expressions for validation.
"""

import re

def validate_phone_number(phone_number):
    pattern = r'^\d{10}$'  # Matches a string of 10 digits
    return re.match(pattern, phone_number) is not None