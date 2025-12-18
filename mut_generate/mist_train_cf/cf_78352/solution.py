"""
QUESTION:
Write a function named `fibonacci(n)` that generates the first `n` numbers in the Fibonacci sequence. The Fibonacci sequence is a series of numbers where a number is found by adding up the two numbers before it. The function should take an integer `n` as input and return a list of the first `n` Fibonacci numbers.
"""

def fibonacci(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence[:n]