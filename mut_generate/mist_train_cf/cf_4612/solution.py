"""
QUESTION:
Write a function gcd(A, B) to find the greatest common divisor of two positive integers A and B, where A > B, without using any arithmetic operations (+, -, *, /) or bitwise operations (&, |, ^, <<, >>). The time complexity of the solution should be O(log min(A, B)).
"""

def gcd(A, B):
    while B != 0:
        A, B = B, A % B
    return A