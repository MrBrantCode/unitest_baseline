"""
QUESTION:
Write a function `first_three_distinct_positions` that takes an array as input and returns the indices of the first three distinct elements in the array. The array may contain duplicates and negative numbers.
"""

def first_three_distinct_positions(array):
    """
    Returns the indices of the first three distinct elements in the array.

    Args:
        array (list): Input array.

    Returns:
        list: Indices of the first three distinct elements.
    """
    positions = []
    count = 0

    for i, num in enumerate(array):
        if num not in array[:i] and count < 3:
            positions.append(i)
            count += 1

    return positions