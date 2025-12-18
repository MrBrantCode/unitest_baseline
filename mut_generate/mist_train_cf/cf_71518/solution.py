"""
QUESTION:
Create a function `decompose_phone_numbers` that takes a string `text` as input and returns a list of dictionaries. Each dictionary should contain the decomposed components of a phone number found in the text: 'country_code', 'area_code', 'local_code', and 'line_number'. Assume phone numbers are in the format +X (XXX) XXX-XXXX.
"""

import re

def decompose_phone_numbers(text):
    """
    Decompose phone numbers found in the input text into their components.

    Args:
        text (str): The input text containing phone numbers.

    Returns:
        list: A list of dictionaries, each containing the decomposed components of a phone number:
            'country_code', 'area_code', 'local_code', and 'line_number'.
    """
    phone_numbers = re.findall(r'\+\d{1,4}\s\(\d{3}\)\s\d{3}-\d{4}', text)
    decomposed_numbers = []

    for phone in phone_numbers:
        decomposed = re.search(r'\+?(?P<country>\d{1,4})\s\((?P<area>\d{3})\)\s(?P<local>\d{3})-(?P<line>\d{4})', phone)
        decomposed_numbers.append({
            'country_code': decomposed.group('country'),
            'area_code': decomposed.group('area'),
            'local_code': decomposed.group('local'),
            'line_number': decomposed.group('line')
        })

    return decomposed_numbers