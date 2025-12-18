"""
QUESTION:
Create a function called `is_valid_us_phone_number` that takes a string as input and returns `True` if the string contains a valid US phone number in the format "(XXX) XXX-XXXX", where the first digit of the area code cannot be 0 or 1, and `False` otherwise.
"""

import re

def is_valid_us_phone_number(phone_number):
    # Check if the string matches the format (XXX) XXX-XXXX
    if not re.match(r'^\(\d{3}\) \d{3}-\d{4}$', phone_number):
        return False
    
    # Extract the area code from the phone number
    area_code = phone_number[1:4]
    
    # Check if the first digit of the area code is not 0 or 1
    if area_code[0] in ['0', '1']:
        return False
    
    return True