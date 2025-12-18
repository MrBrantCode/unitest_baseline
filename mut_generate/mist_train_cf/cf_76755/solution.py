"""
QUESTION:
Design a function `fibonacci(n)` that generates the Fibonacci sequence up to the nth term, where n is a prime number. The function should take an integer `n` as input and return a list of integers representing the Fibonacci sequence.
"""

def fibonacci(n):
    fib_sequence = [0,1]
    while len(fib_sequence)<n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence