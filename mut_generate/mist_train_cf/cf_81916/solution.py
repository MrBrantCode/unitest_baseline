"""
QUESTION:
Implement two functions, `factorial_recursive` and `factorial_iterative`, to calculate the factorial of a given non-negative integer. The `factorial_recursive` function should use recursion, while the `factorial_iterative` function should use an iterative process. Both functions should take one argument `n`, which is the input number for the factorial calculation, and return the calculated factorial.
"""

def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)

def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result