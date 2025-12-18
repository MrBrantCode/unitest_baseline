"""
QUESTION:
Implement a function named `factorial` that calculates the factorial of a positive integer `n` and returns the result along with the number of function calls made. The function should have a time complexity of O(n), not use any loops or iteration, and handle edge cases where `n` is less than 0. The function should also be able to handle large input values and return an error message if `n` is not a non-negative integer.
"""

def factorial(n, count=0):
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1, count
    else:
        result, count = factorial(n - 1, count + 1)
        return n * result, count 