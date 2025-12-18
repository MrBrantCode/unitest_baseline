"""
QUESTION:
Write a function `C(n)` that calculates the number of idempotent 3x3 matrices with integer elements between -n and n. An idempotent matrix is a matrix that satisfies the condition M^2 = M. The function should return the total count of such matrices.
"""

def C(n):
    return 2 * 2 * 2 * (2*n+1) * (2*n+1) * (2*n+1)