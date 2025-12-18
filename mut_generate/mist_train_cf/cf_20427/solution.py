"""
QUESTION:
Write a function named `is_valid_phone_number` that checks if a given string represents a valid phone number. The phone number should start with a plus sign (+) followed by a two-digit country code (between 1 and 99), a hyphen (-), a three-digit area code (between 100 and 999), another hyphen (-), and a 7-digit phone number.
"""

import re

def is_valid_phone_number(phone_number):
    """
    Checks if a given string represents a valid phone number.
    
    A valid phone number should start with a plus sign (+) followed by a two-digit country code (between 1 and 99),
    a hyphen (-), a three-digit area code (between 100 and 999), another hyphen (-), and a 7-digit phone number.

    Args:
        phone_number (str): The phone number to be checked.

    Returns:
        bool: True if the phone number is valid, False otherwise.
    """

    # Define the regular expression pattern for a valid phone number
    pattern = r'^\+[1-9][0-9]?-[1-9][0-9]{2}-[0-9]{7}$'

    # Use the fullmatch function to check if the phone number matches the pattern
    return bool(re.fullmatch(pattern, phone_number))