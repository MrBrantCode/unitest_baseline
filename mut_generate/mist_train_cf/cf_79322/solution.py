"""
QUESTION:
Write a function `special_rounding(value, low, high)` that takes a string `value` representing a number and two integers `low` and `high` as range boundaries. The function should return the closest integer to `value` without using built-in rounding methods. It should also validate if `value` is a valid integer or float and if it falls within the range `[low, high]`. If these conditions are not met, return an error message. When `value` is equidistant from two integers, it should be rounded towards zero.
"""

def special_rounding(value, low, high):
    # Input Validation
    try:
        value = float(value)
    except ValueError:
        return "Error: Invalid input."
    
    # Check if the value is within the range
    if not low <= value <= high:
        return "Error: Out of range."
    
    # Rounding process
    decimal = value - int(value)
    if decimal >= 0.5 and value >= 0:
        value += 1
    elif decimal <= -0.5 and value <= 0:
        value -= 1
    
    return int(value)