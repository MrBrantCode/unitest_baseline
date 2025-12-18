"""
QUESTION:
Create a function named `format_number` that takes two parameters: `number` and `decimal_places`. If `decimal_places` is non-negative, the function should format `number` to the specified number of decimal places. If `decimal_places` is negative, the function should round `number` to the nearest 10th, 100th, 1000th, and so on, depending on the absolute value of `decimal_places`. The function should return the formatted or rounded number as a string.
"""

def format_number(number, decimal_places):
    if decimal_places >= 0:
        return "{:.{}f}".format(number, decimal_places)
    else:
        rounding_factor = 10 ** abs(decimal_places)
        rounded_number = round(number / rounding_factor) * rounding_factor
        return "{:.0f}".format(rounded_number)