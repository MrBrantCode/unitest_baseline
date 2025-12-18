"""
QUESTION:
Create a recursive function named `parity` that takes an integer `n` as input and returns 0 if the total number of 1's in its binary representation is even, and 1 if the total number of 1's is odd. The function should not use any bitwise operations or conventional division/modulus operations to determine the parity. The function should assume 0 has even parity and 1 has odd parity.
"""

def parity(n):
    # Base condition: If n is 0 or 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    power = 1
    
    while power <= n:
        power *= 2

    power /= 2

    return (1 - parity(n - power))