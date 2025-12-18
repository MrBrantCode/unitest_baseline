"""
QUESTION:
Implement a function `fib_memo` that calculates the nth Fibonacci number using memoization to optimize performance. The function should take two parameters: `n`, the position of the Fibonacci number to calculate, and `memo`, a dictionary to store previously calculated Fibonacci numbers.
"""

def fib_memo(n, memo):
    if n <= 1:
        return n

    if n not in memo:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    
    return memo[n]