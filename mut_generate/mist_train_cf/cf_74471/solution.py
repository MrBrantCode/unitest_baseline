"""
QUESTION:
Create a function named `fibonacci_reverse` that takes a non-negative integer `n` as input and returns a list of Fibonacci sequence numbers up to the nth number in reverse order. The function should handle edge cases where `n` is less than or equal to 0 by returning an empty list.
"""

def fibonacci_reverse(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [1, 0]
    else:
        fib = fibonacci_reverse(n - 1)
        fib.insert(0, fib[0] + fib[1])
        return fib