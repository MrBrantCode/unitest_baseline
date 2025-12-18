"""
QUESTION:
Write a function `fib_dp(n)` that calculates the nth Fibonacci number using dynamic programming, where `n` is a non-negative integer. The function should return the nth Fibonacci number, with the Fibonacci sequence defined as a series of numbers where each number is the sum of the two preceding ones, starting with 0 and 1.
"""

def fib_dp(n):
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]