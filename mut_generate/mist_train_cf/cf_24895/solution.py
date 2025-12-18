"""
QUESTION:
Write a function named max_nodes_in_full_binary_tree to calculate the maximum number of nodes in a full binary tree. The function should take the height of the tree as an argument and return the maximum number of nodes. The height of the tree will be a non-negative integer.
"""

def max_nodes_in_full_binary_tree(height: int) -> int:
    """
    Calculate the maximum number of nodes in a full binary tree.

    The maximum number of nodes in a full binary tree with a given height can be calculated using the formula 2^(height + 1) - 1.

    Args:
    height (int): The height of the full binary tree.

    Returns:
    int: The maximum number of nodes in the full binary tree.
    """
    return 2 ** (height + 1) - 1