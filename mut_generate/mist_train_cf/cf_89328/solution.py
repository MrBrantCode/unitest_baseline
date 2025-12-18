"""
QUESTION:
Write a function `fibonacci(n, memo={})` to compute the nth Fibonacci number with a time complexity of O(n) and a space complexity of O(1), given a positive integer `n` and assuming the Fibonacci sequence starts with 0 and 1.
"""

def fibonacci(n, memo={}):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]