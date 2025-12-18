"""
QUESTION:
Write a function named `find_five_digit_number` that takes a string `text` as input and returns the first 5-digit number found in the text, excluding any numbers that are part of a customer ID or phone number format. Assume that customer IDs and phone numbers do not contain 5-digit numbers.
"""

import re

def find_five_digit_number(text):
    """
    Finds the first 5-digit number in the given text, excluding any numbers that are part of a customer ID or phone number format.

    Args:
        text (str): The input text to search for the 5-digit number.

    Returns:
        str: The first 5-digit number found in the text, or None if no such number is found.
    """
    pattern = r'\b(?<!\d)(?<!\d\d)(?<!\d\d\d)(?<!\d\d\d\d)(?<!\d\d\d\d\d)\d{5}\b'
    match = re.search(pattern, text)
    return match.group() if match else None