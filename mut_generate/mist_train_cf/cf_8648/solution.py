"""
QUESTION:
Implement a function named `fibonacci(n)` that calculates the nth Fibonacci number iteratively, where n can be as large as 10^9. The function should avoid recursive calls to improve performance. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.
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