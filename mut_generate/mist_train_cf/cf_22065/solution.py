"""
QUESTION:
Write a function `calculate_parity(n)` that calculates the parity of a given binary number `n` using only bitwise operations. The function should take a positive integer `n` up to 10^9 and return 1 if the number of set bits in the binary representation is odd, and 0 if it is even.
"""

def calculate_parity(n):
    # Count the number of set bits using bitwise AND and right shift
    count = 0
    while n:
        count ^= n & 1
        n >>= 1

    # Return 1 if the number of set bits is odd, 0 otherwise
    return count