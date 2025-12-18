"""
QUESTION:
Create a function named `decimal_to_binary` that takes an integer as input and returns its binary representation as a string. The function should use repeated division by 2 to convert the decimal number to binary, adding the remainder of each division to the left side of the binary string. The function should handle non-negative integers.
"""

def decimal_to_binary(number):
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
    return binary