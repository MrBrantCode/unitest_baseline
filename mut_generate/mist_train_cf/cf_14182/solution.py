"""
QUESTION:
Format a given decimal number as a percent value, rounding to 4 decimal places if necessary. The function should take one argument, a float representing the decimal number. The function should return a string representing the formatted percent value.
"""

def format_percent(decimal_number):
    """
    Format a given decimal number as a percent value, rounding to 4 decimal places if necessary.

    Args:
        decimal_number (float): A float representing the decimal number.

    Returns:
        str: A string representing the formatted percent value.
    """
    return "{:.4f}%".format(decimal_number * 100)