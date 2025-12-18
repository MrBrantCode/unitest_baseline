"""
QUESTION:
Write a function named `fibonacci` to compute the nth Fibonacci number using tabulation methodology. The function should take an integer `n` as input and return the nth Fibonacci number. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two. The function should have a time complexity of O(n).
"""

def fibonacci(n):
    fib = [0, 1] + [0] * (n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]