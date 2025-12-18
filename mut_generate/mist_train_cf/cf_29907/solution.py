"""
QUESTION:
Create a function called `fib_cython` that takes an integer `n` as input and returns the nth Fibonacci number using a recursive approach. The function should be implemented in Cython. The function should handle inputs where `n` is 0 or 1.
"""

def fib_cython(n):
    if n <= 1:
        return n
    else:
        return fib_cython(n-1) + fib_cython(n-2)