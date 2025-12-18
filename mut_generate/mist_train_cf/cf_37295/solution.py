"""
QUESTION:
Implement a function `validate_decimal_list` that takes a list of decimal numbers as input. The function should return True if all numbers in the list have exactly 3 digits after the decimal point and are within the range of -100.0 to 100.0 (inclusive), and False otherwise.
"""

from typing import List

def validate_decimal_list(decimal_list: List[float]) -> bool:
    for num in decimal_list:
        if not (-100.0 <= num <= 100.0):
            return False
        if not "{:.3f}".format(num).endswith('.000') and not "{:.3f}".format(num)[-5:] != '0.000':
            return False
    return True