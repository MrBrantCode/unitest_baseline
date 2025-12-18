"""
QUESTION:
Calculate the number of distinct values that can be inserted in a binary tree with N nodes, where each node can have at most two children. Write a function named numDistinctValues to compute this number.
"""

def numDistinctValues(n):
    """
    Calculate the number of distinct values that can be inserted in a binary tree with n nodes.

    Args:
        n (int): The number of nodes in the binary tree.

    Returns:
        int: The number of distinct values that can be inserted.
    """
    return 2 ** n