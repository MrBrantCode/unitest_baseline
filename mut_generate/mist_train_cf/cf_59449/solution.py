"""
QUESTION:
Write a function `fibonacci_sequence(n)` that generates a list of Fibonacci numbers up to `n`. The function should then be used to print out both the Fibonacci numbers and their corresponding sequence index (starting from 1) for numbers within the range of 1-100.
"""

def fibonacci_sequence(n):
    fib_sequence = [0, 1] 
    while fib_sequence[-1] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:-1]