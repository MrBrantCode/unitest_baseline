"""
QUESTION:
Write a regular expression to match 11-digit phone numbers that start with 6. The expression should match the entire string and only allow digits.
"""

import re

def entrance(phone_number: str) -> bool:
    """
    This function checks if a given phone number matches the pattern of an 11-digit number starting with 6.
    
    Args:
    phone_number (str): The phone number to be checked.
    
    Returns:
    bool: True if the phone number matches the pattern, False otherwise.
    """
    pattern = r"^6\d{10}$"
    return bool(re.match(pattern, phone_number))