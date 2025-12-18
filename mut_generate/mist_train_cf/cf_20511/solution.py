"""
QUESTION:
Implement a function `gcd(A, B)` that calculates the greatest common divisor of two positive integers A and B without using any built-in GCD functions or libraries, the modulus operator (%), or any other division-related operator. The inputs A and B are positive integers where 1 <= A, B <= 10^9.
"""

def gcd(A, B):
    # Check if A is 0, in which case the GCD is B
    if A == 0:
        return B
    
    # Check if B is 0, in which case the GCD is A
    if B == 0:
        return A
    
    # Apply the Euclidean algorithm
    while B != 0:
        A, B = B, A - (A // B) * B
    
    # The GCD is the last non-zero remainder
    return A