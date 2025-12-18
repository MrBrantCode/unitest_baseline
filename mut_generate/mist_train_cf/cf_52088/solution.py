"""
QUESTION:
Create a function `fibonacci(n)` that generates and returns the Fibonacci sequence up to the nth digit, where the sequence starts from 0. The function should take one argument `n`, representing the number of digits in the sequence, and return a list of integers.
"""

def fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1
    for i in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a+b
    return fibonacci_sequence