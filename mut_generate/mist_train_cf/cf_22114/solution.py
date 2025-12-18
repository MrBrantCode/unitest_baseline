"""
QUESTION:
Create a function named `format_decimal_as_percent` that takes a decimal number as input, multiplies it by 100, rounds the result to the nearest whole number, and returns the result as a string with a percent sign. The function should handle decimal numbers with up to 4 decimal places and negative decimal numbers.
"""

def entrance(decimal):
    percent = decimal * 100
    percent = round(percent)
    percent_string = str(percent) + "%"
    return percent_string