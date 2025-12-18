"""
QUESTION:
Write a function `validate_phone_number` that takes a string `phone_number` and a list of strings `restricted_numbers` as input. The function should return `True` if the phone number is valid and not in the list of restricted numbers, and `False` otherwise. 

The phone number is valid if it matches the format XXX-XXX-XXXX where each X represents a digit from 0-9, the country code is a valid two-letter country code according to the ISO 3166-1 alpha-2 standard, it does not have consecutive repeating digits, and it does not have sequential digits.
"""

import re

def validate_phone_number(phone_number, restricted_numbers):
    # Check if the phone number matches the format XXX-XXX-XXXX
    if not re.match(r'^\d{3}-\d{3}-\d{4}$', phone_number):
        return False
    
    # Check if the country code is a valid two-letter country code
    country_code = phone_number[:2]
    valid_country_codes = ['US', 'CA', 'UK']  # Add more valid country codes if needed
    if country_code not in valid_country_codes:
        return False
    
    # Check if the phone number has consecutive repeating digits
    if re.search(r'(\d)\1{2}-\1{3}-\1{4}', phone_number):
        return False
    
    # Check if the phone number has sequential digits
    if re.search(r'(\d{3})-?\1-?\1', phone_number):
        return False
    
    # Check if the phone number is in the restricted numbers list
    if phone_number in restricted_numbers:
        return False
    
    return True