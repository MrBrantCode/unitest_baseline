"""
QUESTION:
Design a function named `fibonacci(n)` that generates the first `n` values of the Fibonacci sequence. The function should return a list of integers. Assume `n` is a positive integer. Analyze the time and space complexity of this function using Big O notation.
"""

def fibonacci(n):
    fib_sequence = [0, 1]
    
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence