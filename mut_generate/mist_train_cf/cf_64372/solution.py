"""
QUESTION:
Implement a function `special_rounding(value, low, high)` that takes a string `value` representing a number, and two integers `low` and `high` representing a range. The function should return the nearest integer to the input `value` without using built-in rounding functions, while ensuring the input is a valid integer or float and falls within the specified range. If the input is not valid or out of range, return an error message. In cases where the number is equidistant from two integers, round towards zero.
"""

def entrance(value, low, high):
    try:
        num = float(value)
    except ValueError:
        return "Error: Invalid input."

    if num < low or num > high:
        return "Error: Out of range."

    # Split the float number into the integer part and decimal part
    int_part = int(num)
    decimal_part = abs(num - int_part)

    # If the decimal part is less than 0.5, round down, else round up
    # It will always round towards zero
    if decimal_part < 0.5:
        return int_part
    else:
        if num >= 0:
            return int_part + 1 # Round up 
        else:
            return int_part - 1 # Round down 