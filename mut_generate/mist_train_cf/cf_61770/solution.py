"""
QUESTION:
Write a function named `fibonacci` that calculates the nth Fibonacci number with a time complexity of O(N). The function should take an integer `n` as input and return the corresponding Fibonacci number. Implement the function using memoization to optimize its time complexity.
"""

def fibonacci(n, memo={}):
    if n <= 1:
        return n
    elif n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]