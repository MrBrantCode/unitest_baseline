"""
QUESTION:
Calculate the maximum depth of a balanced binary tree given its size n. Write a function named max_depth_balanced_binary_tree that takes an integer n as input, representing the size of the binary tree, and returns the maximum possible depth of the tree. The function should assume that the binary tree is balanced and use the base-2 logarithm to calculate the maximum depth. The result should be rounded up to the nearest whole number, as the depth of a binary tree is always an integer value.
"""

import math

def max_depth_balanced_binary_tree(n):
    """
    Calculate the maximum depth of a balanced binary tree given its size n.

    Args:
    n (int): The size of the binary tree.

    Returns:
    int: The maximum possible depth of the tree.
    """
    return math.ceil(math.log2(n + 1))