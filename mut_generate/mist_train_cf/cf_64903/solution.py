"""
QUESTION:
Write a function named `triadic_sequences` that takes a list of integers as input and returns a 2D list where each sublist is a sequence of three consecutive numbers from the input list. The function should return all possible sequences that can be formed from the input list, with the last sequence ending at the last element of the input list.
"""

import numpy as np

def triadic_sequences(progression):
    """
    Generate all possible triadic sequences from the input list of integers.

    Args:
        progression (list): A list of integers.

    Returns:
        list: A 2D list where each sublist is a sequence of three consecutive numbers from the input list.
    """
    matrix = []
    for i in range(len(progression)-2):
        row = []
        for j in range(3):
            row.append(progression[i+j])
        matrix.append(row)
    return matrix