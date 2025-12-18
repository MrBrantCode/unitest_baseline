"""
QUESTION:
Compute the parity of a binary number represented as a string. Write a function named `parity(n)` that takes a binary string `n` as input and returns 0 if the number of 1s in the string is even, and 1 if the number of 1s is odd. The input string is guaranteed to consist only of '0' and '1' characters.
"""

def parity(n):
    result = 0
    for bit in n:
        if bit == '1':
            result ^= 1
    return result