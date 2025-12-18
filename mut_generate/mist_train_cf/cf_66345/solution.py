"""
QUESTION:
Implement a function `fib(n)` that calculates the nth Fibonacci number using memoization, where each number is the sum of the two preceding ones. The function should take an integer `n` as input and return the corresponding Fibonacci number. The function should also use a dictionary to store previously computed Fibonacci numbers to avoid redundant calculations.
"""

def fib(n, memo={}):
    if n in memo:
        return memo[n]   # return stored result
    if n < 2:
        result = n
    else:
        result = fib(n-1, memo) + fib(n-2, memo)
    memo[n] = result  # store result for future use
    return result