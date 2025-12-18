"""
QUESTION:
Write a function named `fibonacci` that generates the Fibonacci sequence, a series where each number is the sum of the two preceding ones, and returns the first `n` values of the sequence. The function should take an integer `n` as input and return a list of integers.
"""

def fibonacci(n):
    fib_sequence = [0, 1]
    
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        
    return fib_sequence