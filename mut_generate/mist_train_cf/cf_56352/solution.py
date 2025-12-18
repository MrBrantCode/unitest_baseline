"""
QUESTION:
Create a function `validate_us_phone_number` that takes a string as input and returns `True` if it represents a valid USA phone number, considering optional country code and common formatting variations, and `False` otherwise. The function should be able to validate phone numbers in the following formats: 1234567890, (123) 456-7890, 123 456 7890, +1 123 456 7890, +1-123-456-7890.
"""

import re

def validate_us_phone_number(phone_number: str) -> bool:
    """
    Validate a USA phone number.

    Args:
        phone_number (str): The phone number to validate.

    Returns:
        bool: True if the phone number is valid, False otherwise.
    """
    phone_regex = re.compile(r'^(?:\+1\s?\-?)?\(?(\d{3})\)?[\s\-]?(\d{3})[\s\-]?(\d{4})$')
    return bool(phone_regex.match(phone_number))