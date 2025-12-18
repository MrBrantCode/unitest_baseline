"""
QUESTION:
Create a function named `validate_phone_number` that takes a string `phone_number` as input and returns a boolean indicating whether the phone number is valid or not. A valid phone number should be in the format "123-456-7890" and may optionally have a country code at the beginning, which can be either "+1" or "001", followed by a space before the actual phone number. The function should use regular expressions for validation.
"""

import re

def validate_phone_number(phone_number):
    pattern = r'^(\+1|001)?\s?\d{3}-\d{3}-\d{4}$'
    return bool(re.match(pattern, phone_number))