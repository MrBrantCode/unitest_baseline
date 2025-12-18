"""
QUESTION:
Create a function `validate_phone_number(phone_number)` that checks if the given string is a valid US phone number. The number may include an international dialing code, area code, and/or separators such as spaces, parentheses, or hyphens. The function should return a boolean indicating whether the phone number is valid.
"""

import re

def validate_phone_number(phone_number):
    pattern = re.compile(
        "^(\+\d{1,2}\s?)?(1\s?)?((\((\d{3})\))|\d{3})[\s\-]?[\d]{3}[\s\-]?[\d]{4}$")
    return bool(pattern.match(phone_number))