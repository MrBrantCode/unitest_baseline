"""
QUESTION:
Write a function `generate_geometric_sequence(start, end, ratio)` that generates a unique geometric sequence of numbers within a given range defined by `start` and `end` with a common `ratio`. The function should only include numbers that are within the range and should not include the number that exceeds the `end` value. The inputs `start`, `end`, and `ratio` should all be positive numbers and `start` should be less than `end`.
"""

def generate_geometric_sequence(start, end, ratio):
    """
    Generates a unique geometric sequence of numbers within a given range defined by `start` and `end` with a common `ratio`.

    Args:
        start (int): The start of the range.
        end (int): The end of the range.
        ratio (int): The common ratio.

    Returns:
        list: A list of numbers representing the geometric sequence.
    """
    sequence = [start]

    # Generate sequence
    while True:
        next_num = sequence[-1] * ratio
        if next_num > end:
            break
        sequence.append(next_num)

    return sequence