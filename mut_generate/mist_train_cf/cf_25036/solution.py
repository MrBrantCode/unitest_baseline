"""
QUESTION:
Write a function `max_nodes_height_balanced_binary_tree` that takes an integer `h` as input and returns the maximum number of nodes in a height-balanced binary tree of height `h`.
"""

def max_nodes_height_balanced_binary_tree(h):
    """
    Calculate the maximum number of nodes in a height-balanced binary tree of height h.
    
    Args:
    h (int): The height of the binary tree.
    
    Returns:
    int: The maximum number of nodes in the binary tree.
    """
    return 2 ** (h + 1) - 1