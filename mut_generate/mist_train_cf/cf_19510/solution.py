"""
QUESTION:
Create a function `factorial(n)` that calculates the factorial of a given number `n` using recursion. The function should return -1 for negative inputs.
"""

def entance(n):
    # Handle negative numbers
    if n < 0:
        return -1
    # Base case: factorial of 0 is 1
    elif n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * entance(n-1)