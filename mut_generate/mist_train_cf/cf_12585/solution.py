"""
QUESTION:
Write a function `max_depth` that calculates the maximum depth of a balanced binary tree of size n. The binary tree is assumed to be perfectly balanced, where every node has two children. Implement the function without using recursion and with a time complexity of O(1).
"""

import math

def max_depth(n):
    """
    Calculate the maximum depth of a balanced binary tree of size n.

    Args:
        n (int): The size of the binary tree.

    Returns:
        int: The maximum depth of the binary tree.
    """
    return math.ceil(math.log2(n + 1))