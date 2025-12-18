"""
QUESTION:
Create a function named `extract_integer` that takes a number (positive or negative float, or string representation of a float in scientific notation) and a precision (integer) as input, and returns the integer part of the number as a float, preserving precision up to the specified decimal point and maintaining trailing zeroes. The function should handle inputs with commas as decimal points and round down to the nearest lower integer if the number is not already an integer.
"""

from decimal import Decimal, ROUND_DOWN

def extract_integer(number: float, precision: int) -> float:
    decimal_point = Decimal(10) ** -precision
    if isinstance(number, (int, float)):
        number = Decimal(number)  
    elif isinstance(number, str):
        number = Decimal(number.replace(',', '.'))

    return float(number.quantize(decimal_point, rounding=ROUND_DOWN))