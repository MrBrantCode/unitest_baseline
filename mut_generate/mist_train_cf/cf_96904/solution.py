"""
QUESTION:
Create a function named `calculate_parity` that takes a positive integer `n` as input and returns 1 if the number of set bits in the binary representation of `n` is odd, and 0 if it is even. The function should use only bitwise operations and handle numbers up to 10^9.
"""

def calculate_parity(n):
    # Count the number of set bits using bitwise AND and right shift
    count = 0
    while n:
        count ^= n & 1
        n >>= 1

    # Return 1 if the number of set bits is odd, 0 otherwise
    return count