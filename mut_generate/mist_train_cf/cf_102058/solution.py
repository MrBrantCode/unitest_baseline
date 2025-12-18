"""
QUESTION:
Write a function named `result` that takes four integer parameters A, B, C, and D. Using the bitwise AND operator, the function should perform operations on A, B, and C (A & 1, B & 2, C & 3) and return the result only if D is greater than 0; otherwise, return 0.
"""

def result(A, B, C, D):
    return (A & 1) & (B & 2) & (C & 3) if D > 0 else 0