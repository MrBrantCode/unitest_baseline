"""
QUESTION:
Create a function named `convert_scientific_notation` that takes a string representing a number in scientific notation as input and returns the equivalent float value. The function should handle both positive and negative exponents, and the input string may contain multiple digits before or after the "e" symbol, as well as a decimal point before or after the "e" symbol.
"""

def convert_scientific_notation(number):
    parts = number.split('e')
    base = float(parts[0])
    exponent = int(parts[1])

    result = base * (10 ** exponent)
    return result