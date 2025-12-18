"""
QUESTION:
Write a function `traverse_tree_map` that takes a dictionary where keys are integers and values are queues of floating point numbers. For each key, compute and return the median of the values in its corresponding queue. The function should use the built-in `statistics` module for calculating the median and the `collections` module for representing the queue.
"""

from collections import deque
from statistics import median

def traverse_tree_map(tree_map):
    """
    Traverse a dictionary where keys are integers and values are queues of floating point numbers.
    For each key, compute and return the median of the values in its corresponding queue.

    Args:
        tree_map (dict): A dictionary with integer keys and deque values of floating point numbers.

    Returns:
        A dictionary with integer keys and their corresponding median values.
    """
    medians = {}
    for key, val_queue in tree_map.items():
        med = median(val_queue)
        medians[key] = med
    return medians