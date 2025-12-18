"""
QUESTION:
Design a function named `special_rounding` that takes a string value and two integer boundaries, `low` and `high`, as inputs. The function should return the nearest integer to the value without using built-in rounding functions. The value should be a valid numeric string, and it must be within the range defined by `low` and `high`. If the value is not valid or out of range, return an error message. If the value is exactly halfway between two integers, round it towards zero.
"""

def special_rounding(value, low, high):
    try:
        float_val = float(value)
        if float_val < low or float_val > high:
            return "Error: Out of range."
    except ValueError:
        return "Error: Invalid input."

    if float_val > 0:
        rounded_val = int(float_val + 0.5)
    else:
        rounded_val = int(float_val - 0.5)
        
    return rounded_val