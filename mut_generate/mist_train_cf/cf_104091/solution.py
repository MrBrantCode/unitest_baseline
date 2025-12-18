"""
QUESTION:
Create a function called `format_number` that takes two parameters: a number and the desired number of decimal places. If the number of decimal places is non-negative, format the number to the specified number of decimal places. If the number of decimal places is negative, round the number to the nearest power of 10 based on the absolute value of the decimal places parameter. Return the formatted or rounded number.
"""

def format_number(number, decimal_places):
    if decimal_places >= 0:
        return "{:.{}f}".format(number, decimal_places)
    else:
        rounding_factor = 10 ** abs(decimal_places)
        rounded_number = round(number / rounding_factor) * rounding_factor
        return "{:.0f}".format(rounded_number)