"""
QUESTION:
Create a function named `lucas` that calculates the nth Lucas number, where the Lucas sequence is defined as: `L(0) = 2, L(1) = 1` and `L(n) = L(n-1) + L(n-2) for n > 1`. The function should be able to handle large values of n without potential issues with stack overflow.
"""

def lucas(n):
    a, b = 2, 1
    for i in range(n):
        a, b = b, a + b 
    return a