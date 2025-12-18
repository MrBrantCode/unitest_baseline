"""
QUESTION:
Create a function named `binary_insertion_sort` that sorts a list of integers in ascending order using the binary search method. The function should take a list of integers as input and return the sorted list.
"""

import bisect

def binary_insertion_sort(collection):
    """Pure implementation of the binary insertion sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    """
    for i in range(1, len(collection)):
        bisect.insort(collection, collection.pop(i), 0, i)
    return collection