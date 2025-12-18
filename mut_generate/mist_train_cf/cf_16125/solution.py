"""
QUESTION:
Write a function named `is_valid_uk_phone_number` that checks if a given string is a valid UK phone number. The string is a valid UK phone number if it meets the following conditions: 

- The string consists of exactly 11 digits.
- The first two digits are between 01 and 99.
- The next three digits are between 000 and 999.
- The last six digits are between 000000 and 999999.

The function should return True if the string is a valid UK phone number and False otherwise.
"""

def is_valid_uk_phone_number(phone_number):
    # Check if the phone number has 11 digits
    if len(phone_number) != 11:
        return False
    
    # Check if the first two digits are in the valid area code range
    area_code = phone_number[:2]
    valid_area_codes = [str(i).zfill(2) for i in range(1, 100)]
    if area_code not in valid_area_codes:
        return False
    
    # Check if the next three digits are valid local area code
    local_area_code = phone_number[2:5]
    if not local_area_code.isdigit() or int(local_area_code) > 999:
        return False
    
    # Check if the last six digits are valid phone number
    phone_digits = phone_number[5:]
    if not phone_digits.isdigit() or int(phone_digits) > 999999:
        return False
    
    return True