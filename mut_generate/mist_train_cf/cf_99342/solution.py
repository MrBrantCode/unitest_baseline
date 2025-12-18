"""
QUESTION:
Write a function named `scientific_to_decimal` that converts a given number in scientific notation to decimal notation. The input is a string in the format "coefficienteexponent" (e.g., "12.5e0"). The function should return the decimal notation of the number as a float.
"""

def scientific_to_decimal(num):
    coefficient, exponent = num.split('e')
    return float(coefficient) * 10 ** int(exponent)