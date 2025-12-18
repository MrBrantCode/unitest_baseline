"""
QUESTION:
Write a recursive function named `fibonacci(n, memo = {})` to calculate the nth Fibonacci number with memoization. The function should take two parameters: `n` (the index of the Fibonacci number to be calculated) and `memo` (a dictionary to store the results of expensive function calls). Implement the function such that it has a time complexity of O(n).
"""

def fibonacci(n, memo = {}):
    if n <= 1:
        return n
    elif n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]