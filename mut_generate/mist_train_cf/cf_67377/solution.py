"""
QUESTION:
Create a function named `special_rounding` that takes a string `value` representing a number and two integers `low` and `high` as input, and returns the closest integer to the input value without using built-in rounding functions. The function should also validate if the provided value is a valid integer or float and whether it lies within the defined range [low, high]. If the input is invalid or out of range, return an error message. In cases where the number is equidistant between two integers, round it towards zero.
"""

def special_rounding(value, low, high):
    # Check if the input value is a valid integer or float
    try:
        num = float(value)
    except ValueError:
        return "Error: Invalid input."

    # Check if the input value is within the defined range (low, high)
    if num < low or num > high:
        return "Error: Out of range."

    # Perform rounding
    if num >= 0:
        int_part = int(num)
        frac_part = num - int_part

        if frac_part < 0.5:
            result = int_part
        else:
            result = int_part + 1
    else:
        num = abs(num)
        int_part = int(num)
        frac_part = num - int_part

        if frac_part < 0.5:
            result = -int_part
        else:
            result = -(int_part + 1)

    return result