"""
QUESTION:
Write a function `fibonacci(n)` that generates the Fibonacci sequence up to the nth term, where each number in the sequence is the sum of the two preceding ones, starting with 0 and 1.
"""

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence