"""
QUESTION:
Write a function `decimal_to_binary(decimal)` that takes an integer `decimal` as input and returns its binary representation as a string. The function should handle negative decimal numbers by converting them to their two's complement binary representation. The conversion should be implemented without using built-in functions or libraries that directly convert decimal to binary, and should have a time complexity of O(log N), where N is the absolute value of the decimal number. The function should only use bitwise operators and should not use data structures such as arrays or lists. The input decimal number can be up to 10^9 in absolute value.
"""

def decimal_to_binary(decimal):
    if decimal < 0:
        decimal = 2**32 + decimal  # convert negative decimal to its two's complement positive representation

    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2

    return binary