"""
QUESTION:
Create a function `fibonacci` that generates the nth number in the Fibonacci sequence. The Fibonacci sequence is defined as the sum of the two preceding numbers in the sequence. If n is less than or equal to 1, return n; otherwise, return the sum of the two preceding numbers.
"""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)