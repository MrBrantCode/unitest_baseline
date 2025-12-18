"""
QUESTION:
Write a function named `octal_to_hexadecimal` that takes an octal number as input and returns its equivalent representation in hexadecimal. The function should not use any built-in conversion functions and should handle the conversion manually. The input octal number is assumed to be a non-negative integer.
"""

# function to convert octal to hexadecimal
def octal_to_hexadecimal(octal):
    decimal = 0
    base = 1

    while (octal):
        last_digit = octal % 10
        octal = int(octal / 10)

        decimal += last_digit * base
        base = base * 8

    hexadecimal = ""
    hexchars = "0123456789ABCDEF";

    while(decimal!=0):
        hexadecimal = hexchars[(decimal % 16)] + hexadecimal
        decimal = int(decimal / 16)

    return hexadecimal