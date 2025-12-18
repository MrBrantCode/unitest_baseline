"""
QUESTION:
Create a function named `validate_phone_number` that takes two parameters: `phone_number` and `restricted_numbers`. The function should use a regular expression to check if `phone_number` is in the format XXX-XXX-XXXX where each X represents a digit from 0-9. Additionally, the function should also verify that `phone_number` is not in the list `restricted_numbers`. Return True if the phone number is valid and not restricted; otherwise, return False. The `restricted_numbers` parameter should default to an empty list if not provided.
"""

import re

def validate_phone_number(phone_number, restricted_numbers=None):
    if restricted_numbers is None:
        restricted_numbers = []
        
    pattern = r'\d{3}-\d{3}-\d{4}'
    
    if not re.match(pattern, phone_number):
        return False
    
    if phone_number in restricted_numbers:
        return False
    
    return True