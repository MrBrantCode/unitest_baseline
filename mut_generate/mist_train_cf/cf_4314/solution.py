"""
QUESTION:
Write a function called `fibonacci` that generates the Fibonacci series up to the nth number using recursion, without loops or mutable variables, and with a time complexity of O(n). The function should take an integer `n` as input.
"""

def fibonacci(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        result = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        memo[n] = result
        return result