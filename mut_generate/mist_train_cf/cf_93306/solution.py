"""
QUESTION:
Write a recursive function `octal_to_binary` to convert an octal number into its binary representation. The function should take an integer `octal` as input and return its binary representation as a string.
"""

def octal_to_binary(octal):
    # Convert octal number to decimal
    decimal = int(str(octal), 8)
    
    # Convert decimal number to binary and return the binary string
    return bin(decimal)[2:]