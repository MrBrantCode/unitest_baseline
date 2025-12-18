"""
QUESTION:
Create a function named `fibonacci` that takes an integer `n` as input and returns the `n`th number in the Fibonacci sequence, which is the sum of the two preceding numbers in the sequence. If `n` is less than or equal to 1, the function should return `n`.
"""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)