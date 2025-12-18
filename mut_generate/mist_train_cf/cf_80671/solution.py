"""
QUESTION:
Write a function `check_imei(imei)` that checks if the given International Mobile Equipment Identity (IMEI) number is valid. A valid IMEI number is a numeric string with a length of either 14 or 15 digits.
"""

import re

def check_imei(imei):
    pattern = re.compile(r'^\d{14,15}$')
    return bool(pattern.match(imei))