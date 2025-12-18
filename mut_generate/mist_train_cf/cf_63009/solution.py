"""
QUESTION:
In a binary decision tree with p binary predictors, where each internal node leads to two other nodes, write a function named `max_nodes` that calculates the maximum number of leaf nodes and the maximum number of internal nodes, given the number of binary predictors p. The function should return a tuple containing the maximum number of leaf nodes and the maximum number of internal nodes.
"""

def max_nodes(p):
    """
    Calculate the maximum number of leaf nodes and internal nodes in a binary decision tree.

    Args:
    p (int): The number of binary predictors.

    Returns:
    tuple: A tuple containing the maximum number of leaf nodes and the maximum number of internal nodes.
    """
    # Calculate the maximum number of leaf nodes
    max_leaf_nodes = 2 ** p
    
    # Calculate the maximum number of internal nodes
    max_internal_nodes = max_leaf_nodes - 1
    
    return max_leaf_nodes, max_internal_nodes