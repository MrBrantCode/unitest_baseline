"""
QUESTION:
Write a function `convert_scientific_notation` that takes a string representing a number in scientific notation as input and returns the equivalent float value. The input string may have a positive or negative exponent, multiple digits before or after the 'e' symbol, and a decimal point before or after the 'e' symbol.
"""

def convert_scientific_notation(number):
    parts = number.split('e')
    base = float(parts[0])
    exponent = int(parts[1])

    result = base * (10 ** exponent)
    return result