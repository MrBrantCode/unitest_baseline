"""
QUESTION:
Write a function called `find_max_min` that takes a sequence of numbers as input. The sequence must have at least 5 numbers and all numbers must be unique. The function should return a tuple containing the maximum and minimum numbers in the sequence.
"""

def find_max_min(sequence):
    # Check if the sequence has at least 5 numbers
    if len(sequence) < 5:
        return "Sequence must contain at least 5 numbers."

    # Check if the sequence contains duplicates
    if len(sequence) != len(set(sequence)):
        return "Sequence cannot contain duplicates."

    # Find the maximum and minimum numbers
    maximum = max(sequence)
    minimum = min(sequence)

    return maximum, minimum