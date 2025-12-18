"""
QUESTION:
Implement a function named `sum_of_squares` that takes an integer `n` as input and returns the sum of squares of all integers from 0 to `n` (inclusive) within the range of a 64-bit signed integer. The function should handle negative values of `n` by returning "Invalid input". The solution should have a time complexity of O(1) and not use any built-in functions that directly solve the problem.
"""

def sum_of_squares(n):
    if n < 0:
        return "Invalid input"

    result = n * (n + 1) * (2 * n + 1) // 6

    return result