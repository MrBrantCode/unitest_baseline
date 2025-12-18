"""
QUESTION:
Write a function `fib(n)` that generates and returns the first `n` terms of the Fibonacci sequence, where the sequence starts with 0 and 1, and each subsequent term is the sum of the previous two terms. The function should return a list of integers.
"""

def fib(n):
    """
    Generates and returns the first n terms of the Fibonacci sequence.

    Args:
        n (int): The number of terms in the Fibonacci sequence.

    Returns:
        list: A list of integers representing the first n terms of the Fibonacci sequence.
    """
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence[:n]