"""
QUESTION:
Create a function named `factorial(n)` that calculates the factorial of a given non-negative integer `n`. The function should use tail recursion or its iterative equivalent to avoid stack overflow errors for large inputs (greater than 10,000).
"""

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result