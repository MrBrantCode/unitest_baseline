"""
QUESTION:
Write a function `factorial` that takes a non-negative integer `n` as input and returns its factorial using recursion. The function should handle the base case of 0! = 1 and recursively calculate the factorial for larger values of `n`. The function signature should be `def factorial(n: int) -> int:`.
"""

def factorial(n: int) -> int:
    if n == 0:  # Base case: 0! = 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursively calculate factorial