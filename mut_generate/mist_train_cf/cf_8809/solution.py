"""
QUESTION:
Create a function `format_number` that takes a float number, a positive integer `decimal_places`, and a boolean `truncate` as input. The function should format the number to have exactly `decimal_places` decimal places using only bitwise operations for rounding and truncation. If `truncate` is `False`, the function should round the number to the nearest decimal place; if `truncate` is `True`, the function should truncate the decimal part without rounding.
"""

def format_number(num, decimal_places, truncate):
    # Multiply the number by 10 raised to the power of decimal_places to move the decimal point to the right
    num *= 10 ** decimal_places

    # Round the number if necessary
    if not truncate:
        # Add 0.5 to the number before converting it to an integer to round it up if the decimal part is >= 0.5
        num += 0.5

    # Convert the number to an integer using bitwise operations to truncate it
    num = int(num)

    # Divide the number by 10 raised to the power of decimal_places to move the decimal point back to the correct position
    num /= 10 ** decimal_places

    return num