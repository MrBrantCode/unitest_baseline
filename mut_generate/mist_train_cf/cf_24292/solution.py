"""
QUESTION:
Design a function `min_max_finder` that finds the minimum and maximum elements in a collection of numbers using a heap data structure. The function should take a list of integers as input and return a tuple containing the minimum and maximum values.
"""

import heapq

def min_max_finder(numbers):
    """
    This function finds the minimum and maximum elements in a collection of numbers using a heap data structure.

    Args:
        numbers (list): A list of integers.

    Returns:
        tuple: A tuple containing the minimum and maximum values.
    """
    # Convert the list into a min-heap
    min_heap = numbers[:]
    heapq.heapify(min_heap)

    # Convert the list into a max-heap
    max_heap = [-x for x in numbers]
    heapq.heapify(max_heap)

    # The minimum value is the root of the min-heap
    min_val = min_heap[0]

    # The maximum value is the negative of the root of the max-heap
    max_val = -max_heap[0]

    return min_val, max_val