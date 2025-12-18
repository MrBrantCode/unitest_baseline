"""
QUESTION:
Implement a recursive function `factorial(N)` that takes a non-negative integer `N` as input and returns its factorial. The function should use recursion to calculate the factorial, where the factorial of 0 is defined to be 1.
"""

def entance(N):
    if N == 0:  
        return 1
    return N * entance(N-1)