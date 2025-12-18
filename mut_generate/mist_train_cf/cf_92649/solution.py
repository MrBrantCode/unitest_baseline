"""
QUESTION:
Implement a recursive function called `fibonacci(n)` that calculates the nth Fibonacci number, where `n` is a non-negative integer. The function should have a time complexity of O(n) and a space complexity of O(n).
"""

def fibonacci(n, memo={}):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Memoization
    elif n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]