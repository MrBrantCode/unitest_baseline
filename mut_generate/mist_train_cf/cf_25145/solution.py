"""
QUESTION:
Create a function `generate_fibonacci_sequence` that generates a Fibonacci sequence with a specified length. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. The function should take an integer `length` as input and return a list of integers representing the Fibonacci sequence.
"""

def generate_fibonacci_sequence(length):
    """
    Generates a Fibonacci sequence with a specified length.

    Args:
        length (int): The length of the Fibonacci sequence.

    Returns:
        list: A list of integers representing the Fibonacci sequence.
    """
    sequence = []
    current_val, next_val = 0, 1
    for i in range(length):
        sequence.append(current_val)
        current_val, next_val = next_val, current_val + next_val
    return sequence