"""
QUESTION:
Write a function named `generate_fibonacci_sequence` that generates a Fibonacci sequence of a given length and returns the sequence starting from the 5th element. The function should take an integer `n` as input, representing the length of the Fibonacci sequence.
"""

def generate_fibonacci_sequence(n):
    """
    Generates a Fibonacci sequence of a given length and returns the sequence starting from the 5th element.

    Args:
        n (int): The length of the Fibonacci sequence.

    Returns:
        list: The Fibonacci sequence starting from the 5th element.
    """
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
    return fibonacci_sequence[4:]