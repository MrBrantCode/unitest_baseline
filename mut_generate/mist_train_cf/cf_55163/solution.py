"""
QUESTION:
Write a function `factorial_and_sum` that takes a positive integer `n` and returns the sum of the factorials of all integers from 1 to `n` using recursion. The function should handle edge cases where `n` is a non-integer or a negative integer, and return an error message in these cases.
"""

def factorial_and_sum(n):
    # dealing with edge cases
    if not isinstance(n, int):
        return ("Error: Input must be an integer")
    if n < 0:
        return ("Error: Input must be a positive integer")
    if n == 0:
        return 0

    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    if n == 1:
        return factorial
    else:
        return factorial + factorial_and_sum(n - 1)