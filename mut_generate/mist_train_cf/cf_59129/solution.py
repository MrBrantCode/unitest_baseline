"""
QUESTION:
Create a function `is_number_greater_than_zero` that takes a string as input and returns True if the string represents a positive integer greater than zero, and False otherwise. The function should accept strings with leading zeros (e.g., "00002") but should not accept strings representing non-positive integers, floating-point numbers, or non-numeric values.
"""

import re

def is_number_greater_than_zero(num):
    pattern = r"^0*[1-9]\d*$"
    if re.match(pattern, num):
        return True
    else:
        return False