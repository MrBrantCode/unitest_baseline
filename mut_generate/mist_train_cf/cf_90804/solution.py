"""
QUESTION:
Create a function `validate_phone_number` that takes two parameters: `phone_number` and `restricted_numbers`. The `phone_number` parameter is a string representing a phone number in the format XXX-XXX-XXXX, where each X is a digit from 0-9. The `restricted_numbers` parameter is a list of phone numbers in the same format that are not allowed. The function should return `True` if the `phone_number` is in the correct format and not in the `restricted_numbers` list, and `False` otherwise.
"""

import re

def validate_phone_number(phone_number, restricted_numbers):
    pattern = r'\d{3}-\d{3}-\d{4}'
    
    if not re.match(pattern, phone_number):
        return False
    
    if phone_number in restricted_numbers:
        return False
    
    return True