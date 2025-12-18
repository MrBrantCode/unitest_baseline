"""
QUESTION:
Implement a function `find_phone(text: str) -> List[str]` that extracts phone numbers from a given text and returns a list of unique phone numbers in the format "XXX-XXX-XXXX". A phone number is defined as a sequence of 10 digits, possibly separated by hyphens or spaces in a specific pattern. The function should handle various formats of phone numbers and the input text can be of maximum length 10^6 characters.
"""

import re
from typing import List

def find_phone(text: str) -> List[str]:
    phone_pattern = re.compile(r'(\d{3}[-\s]?\d{3}[-\s]?\d{4})')
    matches = phone_pattern.findall(text)
    unique_phone_numbers = list(set([re.sub(r'[-\s]', '', match) for match in matches]))
    return unique_phone_numbers