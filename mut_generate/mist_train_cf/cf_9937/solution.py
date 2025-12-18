"""
QUESTION:
Write a function `bitwise_and` that takes three integers A, B, and C as input and returns a boolean value. The function should return True if and only if (A & 1) and (B & 2) and (C & 3) are all True. The function should use the bitwise AND operator (&) instead of the logical AND operator (and).
"""

def bitwise_and(A, B, C):
    return (A & 1) & (B & 2) & (C & 3)