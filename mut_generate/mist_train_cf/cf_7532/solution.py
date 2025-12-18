"""
QUESTION:
Write a function named `calculate_parity` that takes an integer as input and returns its parity. The function should use only bitwise operations and handle integers up to 10^18. If the input is negative, the function should return -1. If the number of set bits in the binary representation is odd, the function should return 1; otherwise, it should return 0.
"""

def calculate_parity(number):
    if number < 0:
        return -1

    number ^= number >> 32
    number ^= number >> 16
    number ^= number >> 8
    number ^= number >> 4
    number ^= number >> 2
    number ^= number >> 1

    return number & 1