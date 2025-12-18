"""
QUESTION:
Write a function named `convert_octal` that takes an octal number as a string, converts it to decimal, binary, and hexadecimal, and returns the results. The function should handle invalid input by catching and handling the ValueError exception.
"""

def convert_octal(octal):
    try:
        decimal = int(octal, 8)
        binary = bin(decimal)[2:]
        hexadecimal = hex(decimal)[2:]
        return decimal, binary, hexadecimal
    except ValueError:
        print("Invalid octal number")