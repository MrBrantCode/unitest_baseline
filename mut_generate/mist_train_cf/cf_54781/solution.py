"""
QUESTION:
Implement a function `fib` that calculates the n-th Fibonacci number using memoization to avoid repeated calculations and reduce time complexity. The function should take an integer `n` as input and return the corresponding Fibonacci number. The function should be able to handle large values of `n` without causing a stack overflow error.
"""

def fib(n, memo):
    if n <= 1:
        return 1
    elif memo[n] != 0:
        return memo[n]
    else:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
        return memo[n]