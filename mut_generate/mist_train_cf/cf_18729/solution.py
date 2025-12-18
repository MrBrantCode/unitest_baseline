"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given integer `n` using a while loop. The function should return the factorial of `n`. Ensure the function handles the base cases where `n` is 0 or 1.
"""

def entance(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result