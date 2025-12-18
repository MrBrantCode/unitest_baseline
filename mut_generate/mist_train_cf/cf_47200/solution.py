"""
QUESTION:
Write a function called `format_currency` that takes a decimal number as input and returns a string representing the decimal number in USD currency format, with commas as thousand separators and rounded to two decimal places.
"""

def format_currency(decimal_num):
    return "${:,.2f}".format(decimal_num)