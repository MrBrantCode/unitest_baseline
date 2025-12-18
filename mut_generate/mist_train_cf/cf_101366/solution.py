"""
QUESTION:
Write a function `fibonacci(n, memo={})` that calculates the nth number in the Fibonacci sequence using both recursive functions and dynamic programming techniques. The function should store previously calculated values in a dictionary called `memo` to avoid redundant calculations.
"""

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    elif n <= 1:
        return n
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]