"""
QUESTION:
Create a function `validate_phone_number` that takes a string `phone_number` as input. The function should validate the phone number using regular expressions, with the following requirements: 
- The phone number can optionally start with either "+1" or "001", followed by a space.
- The phone number should be in the format "123-456-7890" (with or without the country code).
- The phone number should not contain any repeating digits.
Return `True` if the phone number is valid and `False` otherwise.
"""

import re

def validate_phone_number(phone_number):
    # Regular expression for phone number validation
    pattern = r'^(\+1|001)\s?\d{3}-\d{3}-\d{4}$'
    
    # Check if phone number matches the pattern
    if re.match(pattern, phone_number):
        # Remove country code and space from phone number
        phone_number = re.sub(r'^(\+1|001)\s?', '', phone_number)
        
        # Check for repeating digits
        if len(set(phone_number.replace("-", ""))) == len(phone_number.replace("-", "")):
            return True
    
    return False