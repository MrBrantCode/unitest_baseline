"""
QUESTION:
Create a function called `fibonacci(n)` that generates a Fibonacci sequence up to n elements. The function should take an integer `n` as input, where `n` represents the quantity of terms in the sequence. The function should return a list of integers representing the Fibonacci sequence.
"""

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]