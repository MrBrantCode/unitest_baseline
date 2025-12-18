"""
QUESTION:
Create a function `validate_phone_number(number)` that validates a phone number string in the format +{country_code}-{area_code}-{number}, where {country_code} is a string of up to 3 digits, {area_code} is a string of up to 3 digits, and {number} is a string of 4 to 10 digits. The function should return True if the phone number is valid and False otherwise.
"""

import re

def validate_phone_number(number):
    """
    Validates a phone number string in the format +{country_code}-{area_code}-{number}.
    Returns True if valid, False otherwise.
    """
    pattern = r'^\+\d{1,3}-\d{1,3}-\d{4,10}$'
    return bool(re.match(pattern, number))