"""
QUESTION:
Implement a function `validate_phone_number(phone_number: str) -> bool` that takes a string `phone_number` as input and returns `True` if the phone number is valid based on the following rules: 
- The phone number must consist of only digits (0-9) and may contain optional hyphens (-) and parentheses ().
- If the phone number contains optional hyphens or parentheses, they must be placed correctly according to the standard phone number format.
- The phone number must have a minimum length of 10 characters and a maximum length of 14 characters, including optional hyphens and parentheses.
"""

import re

def validate_phone_number(phone_number: str) -> bool:
    cleaned_number = re.sub(r'\D', '', phone_number)

    if len(cleaned_number) < 10 or len(cleaned_number) > 14:
        return False

    return bool(re.match(r'^\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{4})$', phone_number))