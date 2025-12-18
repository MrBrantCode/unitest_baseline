"""
QUESTION:
Write a function called `extract_digits` that takes a string representation of a number as input and returns a list of its digits. The function should support positive and negative numbers with decimal points, exponential notation, hexadecimal format, complex numbers, and scientific notation. The function should handle numbers up to 10^100, with up to 100 digits before the 'e' in exponential notation and up to 10 digits after the 'e'. For complex numbers, the function should return two separate lists of digits for the real and imaginary parts. For scientific notation, the function should return two separate lists of digits for the coefficient and exponent.
"""

import re

def extract_digits(number):
    # Handle hexadecimal format
    if number.startswith("0x"):
        number = str(int(number, 16))

    # Handle complex numbers
    if "+" in number:
        real, imaginary = number.split("+")
        real_digits = re.findall(r"\d", real)
        imaginary_digits = re.findall(r"\d", imaginary)
        return real_digits, imaginary_digits

    # Handle scientific notation
    if "e" in number:
        coefficient, exponent = number.split("e")
        coefficient_digits = re.findall(r"\d", coefficient)
        exponent_digits = re.findall(r"\d", exponent)
        return coefficient_digits, exponent_digits

    # Handle regular numbers
    digits = re.findall(r"\d", number)
    return digits