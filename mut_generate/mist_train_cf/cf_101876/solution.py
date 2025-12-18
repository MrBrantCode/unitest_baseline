"""
QUESTION:
Create a function named `convert_octal` that takes an octal number as input and returns its decimal, binary, and hexadecimal representations. The function should handle invalid inputs and return an error message if the input is not a valid octal number.
"""

def convert_octal(octal):
    try:
        decimal = int(octal, 8)
        binary = bin(decimal)[2:]
        hexadecimal = hex(decimal)[2:]
        return decimal, binary, hexadecimal
    except ValueError:
        return "Invalid octal number"