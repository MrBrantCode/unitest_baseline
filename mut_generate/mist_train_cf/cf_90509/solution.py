"""
QUESTION:
Implement an iterative function `fibonacci(n)` to calculate the nth Fibonacci number, where `n` can be as large as 10^9. The function should avoid recursive calls and have a time complexity better than the naive recursive solution. The function should return the nth Fibonacci number for a given non-negative integer `n`.
"""

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]

    return fib[n]