"""
QUESTION:
Write a function named `convert_octal` that takes an octal number as input and returns a tuple containing its decimal, binary, and hexadecimal representations. The function should handle invalid octal numbers by printing an error message.
"""

def convert_octal(octal):
    try:
        decimal = int(octal, 8)
        binary = bin(decimal)[2:]
        hexadecimal = hex(decimal)[2:]
        return decimal, binary, hexadecimal
    except ValueError:
        print("Invalid octal number")