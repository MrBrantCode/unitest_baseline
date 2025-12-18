"""
QUESTION:
Create a function called `is_valid_uk_phone_number` that checks if a given string is a valid UK phone number. The function should take one string argument and return a boolean value.

The function must follow these rules to determine if a string is a valid UK phone number:
- The phone number consists of 11 digits.
- The first two digits are the area code, which can be any number between 01 and 99.
- The next three digits are the local area code, which can be any number between 000 and 999.
- The last six digits are the phone number itself, which can be any number between 000000 and 999999.

The function should have a time complexity of O(1) and a space complexity of O(1).
"""

def is_valid_uk_phone_number(phone_number):
    if len(phone_number) != 11:
        return False

    area_code = phone_number[:2]
    local_area_code = phone_number[2:5]
    phone_number_digits = phone_number[5:]

    if not area_code.isdigit() or not local_area_code.isdigit() or not phone_number_digits.isdigit():
        return False

    area_code = int(area_code)
    local_area_code = int(local_area_code)
    phone_number_digits = int(phone_number_digits)

    if area_code < 1 or area_code > 99 or local_area_code < 0 or local_area_code > 999 or phone_number_digits < 0 or phone_number_digits > 999999:
        return False

    return True