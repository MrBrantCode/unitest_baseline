"""
QUESTION:
Write a function `find_phone_numbers` that takes a string `subject` as input and returns all phone numbers with a pattern of 10 digits. The phone number must start with a digit between 2-9 for both the first three digits and the next three digits, and the last four digits can be any numbers from 0-9. The function should return the phone numbers in the format 'XXX-XXX-XXXX' and should reject invalid phone numbers.
"""

import re

def find_phone_numbers(subject):
    # Regular expression pattern for a valid phone number
    pattern = r'\b([2-9]\d{2})\-([2-9]\d{2})\-(\d{4})\b'

    # Find all matching phone numbers
    matches = re.findall(pattern, subject)

    # Format and return all matched phone numbers
    return [f'{m[0]}-{m[1]}-{m[2]}' for m in matches]