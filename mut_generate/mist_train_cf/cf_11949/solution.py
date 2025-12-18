"""
QUESTION:
Write a function called `fibonacci` that takes an integer `n` as input and returns a list of the first `n` Fibonacci numbers in O(n) time complexity. The Fibonacci sequence is defined such that each number is the sum of the two preceding ones, usually starting with 0 and 1.
"""

def fibonacci(n):
    if n <= 0:
        return []

    fib_sequence = [0, 1]  # Initialize Fibonacci sequence with first two numbers

    # Calculate Fibonacci numbers up to n
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

    return fib_sequence[:n]