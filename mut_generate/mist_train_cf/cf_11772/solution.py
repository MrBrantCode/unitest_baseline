"""
QUESTION:
Write a recursive function `factorial(n)` that calculates the factorial of a non-negative integer `n`. The function should have at least two base cases and demonstrate the proper use of recursive calls. The function should return the correct result for any non-negative integer input `n`.
"""

def entance(n):
    # Base case 1: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1

    # Recursive call: factorial of n is n multiplied by factorial of (n-1)
    return n * entance(n - 1)