"""
QUESTION:
Write a function `check_decimal(s)` that checks if a given string `s` is a decimal number with a precision of up to 4 decimal places, positive, and falls within the range 0 to 10000. The function should also handle scientific notation (e.g., 1.23e3).
"""

import re

def check_decimal(s):
    # Check if it's a normal decimal or scientific notation
    if re.match("^\d+(?:\.\d{1,4})?$", s) or re.match("^\d+(?:\.\d{1,4})?[eE][+-]?\d+$", s):
        # Convert the string to a float
        num = float(s)
        # Check if it's positive and within the range
        if 0 <= num <= 10000:
            return True
        else:
            return False
    else:
        return False