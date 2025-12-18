"""
QUESTION:
Design a recursive function named `sum_of_squares` that calculates the sum of the squares of the numbers between 1 and a given integer `n`. The function should convert negative input values of `n` to positive values, check for non-integer inputs and return an error message, handle large input values of `n` efficiently, and utilize memoization to store previously calculated results. The function should run in O(log(n)) time complexity.
"""

def sum_of_squares(n, memo={}):
    if not isinstance(n, int):
        return "Error: Input value must be an integer."
    n = abs(n)
    if n == 0 or n != int(n):
        return "Error: Input value must be a positive integer."
    if n in memo:
        return memo[n]
    if n == 1:
        memo[n] = 1
        return 1
    result = sum_of_squares(n - 1, memo) + n**2
    memo[n] = result
    return result