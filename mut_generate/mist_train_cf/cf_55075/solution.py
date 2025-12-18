"""
QUESTION:
Create a function named `advanced_complex_rounding` that takes four parameters: `value`, `low`, `high`, and `rounding_type`. The function should take a number as a string (`value`), integer limits (`low` and `high`), and a `rounding_type` parameter that can be one of 'towards_zero', 'floor', or 'ceiling'. The function should check if the input number is a valid integer or floating-point value within the given bounds. Depending on the `rounding_type`, it should round the number to the nearest integer according to the specified rounding type and return the result. If the input number is invalid or outside the range, it should return an error message.
"""

import math

def advanced_complex_rounding(value, low, high, rounding_type):
    try:
        num = float(value)
    except ValueError:
        return "Error: Invalid input."
        
    if not low <= num <= high:
        return "Error: Outside range."
        
    if rounding_type == "towards_zero":
        rounded = int(num) if num >= 0 else -int(-num)
    elif rounding_type == "floor":
        rounded = math.floor(num)
    elif rounding_type == "ceiling":
        rounded = math.ceil(num)
    else:
        return "Error: Invalid rounding type."
    return rounded