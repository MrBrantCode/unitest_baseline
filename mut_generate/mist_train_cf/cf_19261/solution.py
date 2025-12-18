"""
QUESTION:
Calculate the number of distinct values that can be inserted into a balanced binary tree containing N nodes. The values must be inserted in ascending order to keep the tree balanced. The function should take an integer N as input and return the number of distinct values that can be inserted.
"""

def numDistinctValues(N):
    """
    Calculate the number of distinct values that can be inserted into a balanced binary tree containing N nodes.

    Args:
    N (int): The number of nodes in the balanced binary tree.

    Returns:
    int: The number of distinct values that can be inserted into the balanced binary tree.
    """
    import math
    # Calculate the height of the tree
    height = math.log2(N + 1)
    # Calculate the number of distinct values that can be inserted
    distinct_values = 2 ** math.floor(height) - 1
    return int(distinct_values)