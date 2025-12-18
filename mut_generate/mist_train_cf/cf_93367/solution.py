"""
QUESTION:
Write a Python function named `find_max_min` that takes a sequence of numbers as input, where the sequence must contain at least 5 unique numbers. The function should return a tuple containing the maximum and minimum numbers from the sequence.
"""

def find_max_min(sequence):
    # Check if the sequence has at least 5 unique numbers
    if len(set(sequence)) < 5:
        return "Sequence must contain at least 5 unique numbers."

    # Find the maximum and minimum numbers
    maximum = max(sequence)
    minimum = min(sequence)

    return (maximum, minimum)