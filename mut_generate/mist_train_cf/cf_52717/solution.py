"""
QUESTION:
Write a function `max_nodes_in_balanced_bst` that calculates the maximum number of nodes a height-balanced binary search tree can have given its height. The height of a tree is defined as the number of edges in the longest path from the root to a leaf node. Assume that the height `h` is variable. The function should take the height `h` as input and return the maximum number of nodes.
"""

def max_nodes_in_balanced_bst(h):
    """
    Calculate the maximum number of nodes a height-balanced binary search tree can have given its height.

    Args:
        h (int): The height of the binary search tree.

    Returns:
        int: The maximum number of nodes in the binary search tree.
    """
    return (2 ** (h + 1)) - 1