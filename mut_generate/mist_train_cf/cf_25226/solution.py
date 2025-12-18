"""
QUESTION:
Write a function that uses regular expression to detect phone numbers with country code in a given string. The phone numbers are in the format of a plus sign (+) followed by 12 digits. The function should return all occurrences of such phone numbers in the string.
"""

import re

def extract_phone_numbers(s):
    return re.findall(r'\+\d{12}', s)