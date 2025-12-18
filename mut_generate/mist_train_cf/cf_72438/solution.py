"""
QUESTION:
Write a function `special_rounding` that takes a string `value` representing a number and two integers `low` and `high` as range limits. The function should return the nearest integer to the input value without using built-in rounding functions. It should check if the given value is a valid integer or float and if it falls within the specified range. If not, it should return an error message. When the number is equidistant from two integers, it should round towards zero.
"""

def special_rounding(value, low, high):
    try:
        num = float(value)
    except ValueError:
        return "Error: Invalid input."

    if not (low <= num <= high):
        return "Error: Out of range."

    num_int = int(num)
    num_decimal = num - num_int

    if num >= 0:
        if num_decimal >= 0.5:
            num_int += 1
    else:
        if num_decimal <= -0.5:
            num_int -= 1

    return num_int