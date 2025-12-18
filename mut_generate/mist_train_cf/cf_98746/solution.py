"""
QUESTION:
Write a Python function named `scientific_to_decimal` that takes a string containing a number in scientific notation (e.g. "12.5e0") as input and returns the decimal notation of the number as a float. The function should handle the conversion by correctly placing the decimal point based on the exponent value.
"""

def scientific_to_decimal(num):
    coefficient, exponent = num.split('e')
    return float(coefficient) * 10 ** int(exponent)