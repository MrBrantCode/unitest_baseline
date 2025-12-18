"""
QUESTION:
Create a function `is_valid_credit_card_number` that takes a string as input and returns a boolean indicating whether the string represents a valid 16-digit credit card number that only contains numerical digits and does not start with zero.
"""

import re

def is_valid_credit_card_number(number):
    match = re.fullmatch(r'[1-9][0-9]{15}', number)
    return match is not None