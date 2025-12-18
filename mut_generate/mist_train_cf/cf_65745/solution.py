"""
QUESTION:
Create a function `factorial_iterative` that calculates the factorial of a given integer `n` using a loop construct. The function should take an integer `n` as input and return its factorial as an integer.
"""

def factorial_iterative(n: int) -> int:
    result = 1

    for i in range(2, n+1):
        result *= i

    return result