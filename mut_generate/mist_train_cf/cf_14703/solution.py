"""
QUESTION:
Write a function named `fibonacci_sequence` that generates the first 20 elements in the Fibonacci sequence, which follows the rule F(n) = F(n-1) + F(n-2), given that F(0) = 0 and F(1) = 1.
"""

def fibonacci_sequence(n=20):
    """
    Generates the first n elements in the Fibonacci sequence.

    Args:
    n (int, optional): The number of elements in the sequence. Defaults to 20.

    Returns:
    list: A list of the first n Fibonacci numbers.
    """
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence
