"""
QUESTION:
Write a function maxDepth(n) that calculates the maximum depth of a binary tree of size n. Assume the binary tree is a perfect binary tree.
"""

import math

def maxDepth(n):
    """
    Calculate the maximum depth of a perfect binary tree of size n.
    
    Args:
    n (int): The size of the binary tree.
    
    Returns:
    int: The maximum depth of the binary tree.
    """
    return math.ceil(math.log2(n))