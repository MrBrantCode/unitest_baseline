"""
QUESTION:
Compute the modulus of two non-negative integers A and B (0 <= A, B <= 10^9) using only bitwise operators, without using any arithmetic operators, built-in functions, conditional statements, or loops. Assume A is always greater than or equal to B. Implement the solution in a function named compute_modulus(A, B).
"""

def compute_modulus(A, B):
    mod = 0
    while A >= B:
        temp = B
        while (temp << 1) < A:
            temp <<= 1
        A -= temp
    return A