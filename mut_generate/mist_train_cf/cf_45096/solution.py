"""
QUESTION:
Write a function named `minHeapify` that takes an array of integers as input and returns the array transformed into a minimum heap. The function should handle duplicate values, negative integers, and zeros. If the array already represents a minimum heap, the function should return the original array. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array.

The minimum heap property is defined as: the parent node is less than or equal to its child node(s). The function should verify the existence of the node's right child before comparing the node's value with the right child's value.
"""

import heapq

def minHeapify(arr):
    """
    Transforms the given array into a minimum heap.

    Args:
    arr (list): The input array of integers.

    Returns:
    list: The transformed array representing a minimum heap.
    """
    heapq.heapify(arr)
    return arr