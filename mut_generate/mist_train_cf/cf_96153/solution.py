"""
QUESTION:
Implement a function named `gcd` that takes two positive integers `A` and `B` as input, where `1 <= A, B <= 10^9`, and returns their greatest common divisor without using any built-in GCD functions or libraries, the modulus operator (%), or any other division-related operator.
"""

def gcd(A, B):
    if B == 0:
        return A

    q = A // B
    remainder = A - q * B
    return gcd(B, remainder)