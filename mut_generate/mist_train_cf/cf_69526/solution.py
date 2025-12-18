"""
QUESTION:
Write a function `max_and_min_nodes` that calculates the maximum number of nodes in a full binary tree and the minimum number of nodes in a non-full binary tree, given the height of the tree. The function should return two values: the maximum number of nodes for a full binary tree and the minimum number of nodes for a non-full binary tree. Assume the height of the tree is a non-negative integer.
"""

def max_and_min_nodes(height):
    """
    Calculate the maximum number of nodes in a full binary tree and 
    the minimum number of nodes in a non-full binary tree, given the height of the tree.

    Args:
        height (int): The height of the binary tree.

    Returns:
        tuple: A tuple containing the maximum number of nodes for a full binary tree 
               and the minimum number of nodes for a non-full binary tree.
    """
    max_nodes = (2 ** height) - 1  # For a full binary tree
    min_nodes = height  # For a tree with minimum number of nodes possible (non-full)
    return max_nodes, min_nodes