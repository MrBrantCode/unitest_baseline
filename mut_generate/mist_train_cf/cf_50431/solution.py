"""
QUESTION:
Write a function named `reverse_fib_sequence` that takes a list of integers representing a Fibonacci sequence as input and returns the reversed list. The function should not generate a new Fibonacci sequence, but rather reverse the order of elements in the input list.
"""

def reverse_fib_sequence(fib_sequence):
    """
    Reverses the order of elements in a given Fibonacci sequence.

    Args:
        fib_sequence (list): A list of integers representing a Fibonacci sequence.

    Returns:
        list: The reversed Fibonacci sequence.
    """
    return fib_sequence[::-1]