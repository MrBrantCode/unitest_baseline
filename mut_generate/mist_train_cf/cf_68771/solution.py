"""
QUESTION:
Create a function `validate_usa_phone_number(number)` that takes a string as input and returns a boolean indicating whether the input string represents a valid United States phone number. The function should accept phone numbers in the formats "(123)456-7890", "123.456.7890", "123-456-7890", and "1234567890", and reject any input containing letters or special characters other than dashes or parentheses.
"""

import re

def validate_usa_phone_number(number):
    pattern = re.compile(r'^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$')
    return bool(pattern.match(number))