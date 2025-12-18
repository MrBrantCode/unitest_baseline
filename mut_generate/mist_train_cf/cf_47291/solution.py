"""
QUESTION:
Write a function `validate_phone_no` to validate an Indian mobile number. The function should accept a string as input and return "Valid" if the number is valid, "Invalid" otherwise. The function should validate the following formats: 

- Numbers with the country calling code, +91
- Numbers with the country calling code, 0091
- Numbers without the country calling code
- Numbers with and without spaces between digits
- Numbers with a "-" after the first 5 digits

The function should reject all other phone number formats.
"""

import re

def validate_phone_no(phone_no):
    pattern = re.compile(r"(^(0091|\+91)?[ ]?([0-9]{10}$)|([0-9]{5}-[0-9]{5}$))")
    if pattern.match(phone_no):
        return "Valid"
    else:
        return "Invalid"