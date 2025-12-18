"""
QUESTION:
Create a function `find_postcodes(text)` that takes a string as input and returns a list of all potential alphanumeric UK postal codes found in the text. The function should validate the codes based on the UK postal code format which consists of one or two letters, one or two digits, a space, one digit, and two letters. The function should be case-insensitive.
"""

import re

def find_postcodes(text):
    # The regular expression pattern for UK postal codes
    pattern = r'[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][ABD-HJLNP-UW-Zabd-hjlnp-uw-z]{2}'
    return re.findall(pattern, text)