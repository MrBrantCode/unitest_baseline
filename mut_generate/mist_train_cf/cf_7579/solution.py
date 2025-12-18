"""
QUESTION:
Write a function `format_decimal_as_percent(decimal)` that takes a decimal number with up to 10 decimal places as input, formats it as a percent value, handles negative decimal numbers, and rounds the final result to the nearest whole number. The function should have a time complexity of O(1) and a space complexity of O(1).
"""

def format_decimal_as_percent(decimal):
    """
    Formats a decimal number as a percent value.

    Args:
        decimal (float): A decimal number with up to 10 decimal places.

    Returns:
        str: The decimal number formatted as a percent value, rounded to the nearest whole number.
    """
    percent = decimal * 100
    rounded_percent = round(percent)
    formatted_percent = "{:.0f}%".format(rounded_percent)
    return formatted_percent