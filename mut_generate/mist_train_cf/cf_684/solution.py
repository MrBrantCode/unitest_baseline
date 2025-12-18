"""
QUESTION:
Write a function called `extract_digits` that takes a string representing a number as input. The function should extract the digits of the number and return them in an array. The input number can be in various formats, including positive or negative, decimal, exponential notation (e.g., 1.23e-45), hexadecimal format (e.g., 0x1A2B3C), complex numbers (e.g., a + bi), and scientific notation (e.g., 3.14 x 10^5). The function should be able to handle numbers up to 10^100.
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
    if "x" in number:
        coefficient, exponent = number.split("x")
        coefficient_digits = re.findall(r"\d", coefficient)
        exponent_digits = re.findall(r"\d", exponent)
        return coefficient_digits, exponent_digits

    # Handle regular numbers
    digits = re.findall(r"\d", number)
    return digits