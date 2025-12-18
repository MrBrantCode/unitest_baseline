"""
QUESTION:
Create a function called `validate_phone` that checks if the input is a valid U.S. phone number. The function should consider a phone number valid if it starts with '+1', followed by a dash, and exactly 10 numerical digits. The function should return `True` if the input is a valid phone number and `False` otherwise.
"""

import re 

def validate_phone(phone_number):
    match = re.search(r'^\+1-\d{10}$', phone_number)
    return match is not None