"""
QUESTION:
Construct a function named `fibonacci` that generates and returns a list of the first `n` numbers from the Fibonacci sequence. The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers, starting with 0 and 1. The function should take an integer `n` as input and return a list of integers. The function should be able to handle any positive integer `n`.
"""

def fibonacci(n):
    """
    Generates and returns a list of the first n numbers from the Fibonacci sequence.

    Args:
        n (int): The number of Fibonacci numbers to generate.

    Returns:
        list: A list of integers representing the first n numbers in the Fibonacci sequence.
    """
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence[:n]