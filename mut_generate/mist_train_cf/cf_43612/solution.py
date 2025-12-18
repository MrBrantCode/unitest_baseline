"""
QUESTION:
Write a function named `decimal_to_binary(n)` that takes a non-negative integer `n` as input and returns its binary representation as a string.
"""

def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n != 0:
        remainder = n % 2
        n = n // 2
        binary = str(remainder) + binary
    return binary