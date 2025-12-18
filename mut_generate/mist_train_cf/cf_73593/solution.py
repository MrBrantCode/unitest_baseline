"""
QUESTION:
Write a function named `fibonacci(n)` that generates the Fibonacci sequence up to the nth number. The function should take an integer `n` as input and return a list of Fibonacci numbers. The sequence should start with 0 and 1, and each subsequent number should be the sum of the previous two numbers. The function should be able to handle any positive integer `n`.
"""

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence