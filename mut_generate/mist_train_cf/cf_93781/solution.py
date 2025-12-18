"""
QUESTION:
Create a function called `validate_phone_number` that takes two parameters: `phone_number` and `restricted_numbers`. The function should validate the phone number using the following rules: 
- The phone number must be in the format of XXX-XXX-XXXX, where each X represents a digit from 0-9.
- The phone number should start with a valid two-letter country code according to the ISO 3166-1 alpha-2 standard.
- The phone number should not have consecutive repeating digits (e.g., 111-111-1111).
- The phone number should not have sequential digits (e.g., 123-456-7890 or 987-654-3210).
- The phone number should not be in the list of restricted phone numbers provided as the `restricted_numbers` parameter.
 
The function should return `True` if the phone number is valid and `False` otherwise.
"""

import re

def validate_phone_number(phone_number, restricted_numbers):
    # Check if the phone number matches the format XXX-XXX-XXXX
    if not re.match(r'^[A-Z]{2}\d{3}-\d{3}-\d{4}$', phone_number):
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
    digits = ''.join(filter(str.isdigit, phone_number))
    for i in range(len(digits) - 2):
        if int(digits[i]) == int(digits[i+1]) - 1 == int(digits[i+2]) - 2:
            return False
        if int(digits[i]) == int(digits[i+1]) + 1 == int(digits[i+2]) + 2:
            return False
    
    # Check if the phone number is in the restricted numbers list
    if phone_number in restricted_numbers:
        return False
    
    return True