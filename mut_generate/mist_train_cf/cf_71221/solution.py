"""
QUESTION:
Design a function `fib(n)` to calculate the `n-th` number in the Fibonacci sequence, where each number is the sum of the two preceding ones, starting from 0 and 1. The function should handle large values of `n` efficiently, avoiding duplicate calculations and optimizing time and space complexity.
"""

def fib(n, memo = {}):
    """
    Calculate the n-th Fibonacci number efficiently using memoization.

    Args:
    n (int): The position of the Fibonacci number to calculate.
    memo (dict): A dictionary to store previously calculated Fibonacci numbers (default is an empty dictionary).

    Returns:
    int: The n-th Fibonacci number.
    """
    if n <= 1:
        return n
    elif n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]