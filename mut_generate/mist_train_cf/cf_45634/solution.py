"""
QUESTION:
Create a function `usd_format(decimal_number)` that takes a decimal number as input and returns the number formatted as a United States Dollar (USD) currency string, using commas to separate every three digits and rounding to two decimal places.
"""

def usd_format(decimal_number):
    usd_currency = "${:,.2f}".format(decimal_number)
    return usd_currency