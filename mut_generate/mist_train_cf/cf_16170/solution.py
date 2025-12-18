"""
QUESTION:
Implement a function `get_second_largest_unique` that takes a sequence of integers as input and returns the second largest unique element. The function should handle sequences of any length, including those with duplicates. If the sequence has less than two unique elements, the function should return `None`.
"""

def get_second_largest_unique(sequence):
    unique_elements = set(sequence)
    sorted_elements = sorted(unique_elements)
    if len(sorted_elements) < 2:
        return None
    return sorted_elements[-2]