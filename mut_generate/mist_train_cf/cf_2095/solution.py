"""
QUESTION:
Create a function named `convert_scientific_notation_to_float` that takes a string representing a number in scientific notation as input and returns its equivalent float value. The function should handle both positive and negative exponents and round the result to 2 decimal places. The input string may contain a decimal point and multiple digits before and after the "e" symbol.
"""

def convert_scientific_notation_to_float(number):
    number = number.lower()
    parts = number.split('e')
    coefficient = float(parts[0])
    exponent = int(parts[1])
    result = coefficient * (10 ** exponent)
    return round(result, 2)