"""
QUESTION:
Generate a sequence of numbers starting from 1 that are not divisible by a given number. Write a function `generate_sequence` that takes an integer `n` as input and returns a list of integers that are not divisible by `n`. The sequence should only contain numbers from 1 to 100.
"""

def generate_sequence(n):
    """
    Generate a sequence of numbers from 1 to 100 that are not divisible by n.

    Args:
    n (int): The number by which the sequence should not be divisible.

    Returns:
    list: A list of integers from 1 to 100 that are not divisible by n.
    """
    return [i for i in range(1, 101) if i % n != 0]