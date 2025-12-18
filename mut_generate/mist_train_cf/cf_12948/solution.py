"""
QUESTION:
Extract phone numbers from a string in the format (XXX) XXX-XXXX. The string may contain multiple phone numbers and other non-numeric characters. The function should return a list of phone numbers in the order they appear in the string. Implement a function called `extract_phone_numbers` that takes a string `text` as input.
"""

import re

def extract_phone_numbers(text):
    phone_numbers = re.findall(r'\(\d{3}\) \d{3}-\d{4}', text)
    return phone_numbers