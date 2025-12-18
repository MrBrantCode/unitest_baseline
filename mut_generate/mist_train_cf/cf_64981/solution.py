"""
QUESTION:
Write a regular expression to match all 5-digit US postal codes. The postal code should consist of exactly 5 digits.
"""

import re

def us_postal_code(zip_code):
    pattern = re.compile(r'^\d{5}$')
    return bool(pattern.match(zip_code))