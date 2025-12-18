"""
QUESTION:
Write a function called `find_phone_number_with_highest_digits` that takes a list of phone numbers as input and returns the phone number with the highest number of digits. The phone numbers may contain special characters such as parentheses, hyphens, or spaces, which should be ignored when comparing the phone numbers. The function should be able to handle phone numbers of any length.
"""

import re

def find_phone_number_with_highest_digits(phone_numbers):
    """
    This function finds the phone number with the highest number of digits in a given list of phone numbers.
    
    Args:
    phone_numbers (list): A list of phone numbers as strings. The phone numbers may contain special characters.

    Returns:
    str: The phone number with the highest number of digits.
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