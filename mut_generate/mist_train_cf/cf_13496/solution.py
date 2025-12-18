"""
QUESTION:
Write a function `fibonacci(n: int) -> int` that calculates the Nth term of the Fibonacci sequence using dynamic programming, where `n` is a positive integer. The Fibonacci sequence is a series of numbers in which each number (after the first two) is the sum of the two preceding ones, starting with 0 and 1. The function should not use recursion or built-in functions/libraries.
"""

def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    fib = [0] * (n+1)
    fib[0] = 0
    fib[1] = 1
    
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    
    return fib[n]