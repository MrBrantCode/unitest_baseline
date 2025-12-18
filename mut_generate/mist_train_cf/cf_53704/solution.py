"""
QUESTION:
Write a recursive function `factorial(n)` that calculates the factorial of a given non-negative integer `n`. The function should only take one integer parameter and return the calculated factorial. The function should handle the base case where `n` is 0 or 1, and recursively call itself for other cases.
"""

def entance(n):
    # Base case: if the number is 0 or 1, the factorial is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: the factorial of a number is the product of the number and the factorial of the number minus 1
    else:
        return n * entance(n-1)