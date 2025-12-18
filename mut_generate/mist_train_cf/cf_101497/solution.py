"""
QUESTION:
Implement a function named `fibonacci(n)` to calculate the nth number in the Fibonacci sequence. The function should use memoization to achieve a time complexity of O(n) and space complexity of O(n), and it should handle cases where `n` is less than 2.
"""

memo = {}

def fibonacci(n):
    if n in memo:
        return memo[n]
    if n < 2:
        memo[n] = n
    else:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]