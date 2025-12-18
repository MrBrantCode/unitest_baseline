"""
QUESTION:
Create a function named `generate_fibonacci_sequence(n)` that generates the Fibonacci sequence of a specified length `n`. The function should return a list of integers representing the Fibonacci sequence. The function should be efficient and have a time complexity of O(n), where `n` is the length of the sequence.
"""

def generate_fibonacci_sequence(n):
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence