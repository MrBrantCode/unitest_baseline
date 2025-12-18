"""
QUESTION:
Write a function named `fibonacci_sequence(n)` that uses recursion to generate the Fibonacci sequence up to the nth number. The function should return a list of integers representing the Fibonacci sequence. The function should handle cases where `n` is 0, 1, or 2.
"""

def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci_sequence(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence