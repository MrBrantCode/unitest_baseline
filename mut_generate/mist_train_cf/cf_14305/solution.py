"""
QUESTION:
Extract all phone numbers from a given string with the function `extract_phone_numbers` where the phone numbers may be formatted in the following ways:
- with or without parentheses around the area code
- with or without an optional country code
- separated by spaces, hyphens, commas, or semicolons
- multiple phone numbers in the string

The function should return a list of the extracted phone numbers.
"""

import re

def extract_phone_numbers(string):
    pattern = r'(\+?\d{0,2}\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4})'
    phone_numbers = re.findall(pattern, string)
    return phone_numbers