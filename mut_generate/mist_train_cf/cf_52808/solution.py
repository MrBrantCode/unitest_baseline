"""
QUESTION:
Write a function named `extract_phone_numbers` that takes a string as input and returns a list of phone numbers found in the string. The function should be able to extract phone numbers in various formats including (202) 555-0123, 703-555-9876, 555.222.3456, and 1 555 333 4444. The function should be efficient and able to handle large strings of text.
"""

import re

def extract_phone_numbers(text):
    # The following regex matches various phone number formats including:
    # (202) 555-0123, 703-555-9876, 555.222.3456, and 1 555 333 4444
    numbers = re.findall(r'\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}', text)
    return numbers