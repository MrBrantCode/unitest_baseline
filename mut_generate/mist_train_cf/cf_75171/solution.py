"""
QUESTION:
Write a function named `heapMedian` that takes a list of integers as input and returns the median of the list. If the list is empty or has an even number of elements, the function should return None. The function should be optimized for time complexity, ideally achieving O(n).
"""

import statistics

def heapMedian(lst):
    if not lst or len(lst) % 2 == 0:
        return None

    return statistics.median_low(lst)