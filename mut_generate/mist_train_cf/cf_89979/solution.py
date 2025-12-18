"""
QUESTION:
Write a function `calculate_parity(number)` that calculates the parity of a given binary number using only bitwise operations. The function should return 1 if the number of set bits in the binary representation is odd, 0 if it is even, and -1 if the input number is negative. The function should handle numbers up to 10^18.
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