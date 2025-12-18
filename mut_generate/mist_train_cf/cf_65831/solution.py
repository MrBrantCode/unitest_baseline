"""
QUESTION:
Create a function named `fibonacci(n)` that generates the first `n` numbers in the Fibonacci series, where each successive number is the sum of the two preceding numbers, starting with 0 and 1. The function should return a list of the first `n` Fibonacci numbers.
"""

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]