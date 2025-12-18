"""
QUESTION:
Create a function named `extract_phone_numbers` that takes a string `text` as input and returns a list of phone numbers extracted from the string. The function should be able to identify and extract phone numbers with variable number of digits, considering variations in phone number length and country codes. The function should ignore extraneous text around the phone number and recognize both local and international phone numbers, as well as phone numbers with special characters such as parenthesis, dashes, or periods.
"""

import re

def extract_phone_numbers(text):
    pattern = r"(?:(?:\+|00)\d{1,3}\s*)?(?:\d{2,3}[\s.-]*){3,5}\d{2,3}"
    return re.findall(pattern, text)