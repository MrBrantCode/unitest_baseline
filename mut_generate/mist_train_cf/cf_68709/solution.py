"""
QUESTION:
Create a function named `fibonacci(n)` that generates the first `n` elements of the Fibonacci sequence, where each number is the sum of the two preceding ones. The function should be computationally efficient and consider memory usage. The input `n` will be a positive integer.
"""

def fibonacci(n):
    fib_sequence = [0, 1] 
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2]) 
    return fib_sequence[:n]  