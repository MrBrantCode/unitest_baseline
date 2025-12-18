"""
QUESTION:
Create a regular expression function `extract_phone_numbers` that can accurately identify and extract phone numbers from a given text input with a variable number of digits, considering variations in phone number length and country codes. The function should ignore extraneous text around the phone number and recognize local and international phone numbers with special characters such as parenthesis, dashes, or periods.
"""

import re

def extract_phone_numbers(text):
    """
    Extracts phone numbers from a given text input with variable number of digits, 
    considering variations in phone number length and country codes.

    Args:
        text (str): The input text that may contain phone numbers.

    Returns:
        list: A list of phone numbers found in the input text.
    """
    pattern = r"(?:(?:\+|00)\d{1,3}\s*)?(?:\d{2,3}[\s.-]*){3,5}\d{2,3}"
    matches = re.findall(pattern, text)
    return matches