"""
QUESTION:
Write a recursive function named `fibonacci` to compute the nth Fibonacci number with a time complexity of O(n) and a space complexity of O(1). The function should take a positive integer `n` as a parameter and return the corresponding Fibonacci number.
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