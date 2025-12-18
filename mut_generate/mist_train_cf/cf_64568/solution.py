"""
QUESTION:
Create a function named `usd_formatter` that converts a base-10 numerical value into a standardized dollar (USD) currency format. The function should handle negative values and return a proper currency formatted representation, rounding the amount to the nearest dollar. The function should format the output with a comma as a thousand separator and two decimal places.
"""

def usd_formatter(amount):
    rounded_amount = round(amount)
    return "${:,.2f}".format(rounded_amount)