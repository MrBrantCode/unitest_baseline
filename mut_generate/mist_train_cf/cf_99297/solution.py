"""
QUESTION:
Write a function `convert_octal(octal)` that converts a given octal number to its decimal, binary, and hexadecimal representations. The function should take an octal number as input, attempt to convert it to decimal using base 8, and then convert the decimal number to binary and hexadecimal. If the input is not a valid octal number, the function should handle the error and print an error message.
"""

def convert_octal(octal):
    try:
        decimal = int(octal, 8)
        binary = bin(decimal)[2:]
        hexadecimal = hex(decimal)[2:]
        return decimal, binary, hexadecimal
    except ValueError:
        print("Invalid octal number")