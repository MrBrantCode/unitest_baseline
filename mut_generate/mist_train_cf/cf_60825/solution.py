"""
QUESTION:
Write a function named `fibonacci(n)` that generates the initial N numbers in the Fibonacci sequence, starting from 0 and 1 where each subsequent number is the sum of the previous two. The solution should be efficient with a time complexity in mind and handle large values of N.
"""

def fibonacci(n):
    fib_sequence = [0, 1] + [0]*(n-2)
    for i in range(2, n):
        fib_sequence[i] = fib_sequence[i-1] + fib_sequence[i-2]
    return fib_sequence