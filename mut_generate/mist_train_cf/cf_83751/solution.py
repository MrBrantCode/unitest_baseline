"""
QUESTION:
Create a function `validate_phone_number` that takes a string as input and returns True if the string matches any of the following mobile phone number formats, and False otherwise:
- E.164 format (e.g., +1234567890)
- National format with and without area code (e.g., (123) 456-7890, 456-7890)
- Number with hyphens or spaces as separators (e.g., 123-456-7890, 123 456 7890)
- Number with a leading zero (e.g., 0123 456 7890)

The function should be implemented using a regular expression pattern.
"""

import re

def validate_phone_number(phone_number: str) -> bool:
    """
    Validate a phone number against common formats.

    Args:
    phone_number (str): The phone number to validate.

    Returns:
    bool: True if the phone number matches any of the supported formats, False otherwise.
    """
    pattern = r"^(?:\+?(\d{1,3}))?[-. (]*(?:\d{1,4})[-. )]*(\d{1,3})[-. ]*(\d{2,4})$"
    return bool(re.match(pattern, phone_number))