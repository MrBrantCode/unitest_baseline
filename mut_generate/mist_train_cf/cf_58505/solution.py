"""
QUESTION:
Write a function called `fibonacci(n)` that generates the first n elements of the Fibonacci sequence, where each number is the sum of its two preceding numbers. The function should start with a list containing the first two numbers in the sequence, 0 and 1, and continue generating numbers until it reaches the nth number. The function should return a list of the first n numbers in the sequence.
"""

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]