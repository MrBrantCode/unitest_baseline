"""
QUESTION:
Write a function `highest_digits_phone_number` that takes a list of phone numbers as input, where the phone numbers may contain special characters, and returns the phone number with the most digits. The function should consider only the digits when comparing the phone numbers. The phone numbers can be of any length and may contain varying numbers of digits.
"""

import re

def highest_digits_phone_number(phone_numbers):
    """
    Returns the phone number with the most digits from a given list of phone numbers.

    Args:
        phone_numbers (list): A list of phone numbers as strings, possibly containing special characters.

    Returns:
        str: The phone number with the most digits.
    """
    max_digits = 0
    max_number = ""

    for number in phone_numbers:
        # Remove all non-digit characters from the phone number
        digits = re.sub(r"\D", "", number)
        
        # Check if the current number has more digits than the previous max
        if len(digits) > max_digits:
            max_digits = len(digits)
            max_number = number

    return max_number