"""
QUESTION:
Write a function named `fibonacci` that takes two parameters: `n` and `memo`. The function should calculate the `n`th number in the Fibonacci sequence using recursion. The time complexity of the function should not exceed O(n). The function should store previously calculated Fibonacci numbers in the `memo` dictionary to avoid redundant computations. The base case is when `n` is less than or equal to 2, in which case the Fibonacci number is 1. Assume `n` is positive.
"""

def fibonacci(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]