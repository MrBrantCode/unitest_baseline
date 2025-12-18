"""
QUESTION:
Given a fully balanced K-ary tree of depth N, find the proportion between the count of non-leaf nodes and the aggregate count of nodes.
"""

def non_leaf_node_proportion(k, n):
    """
    Calculate the proportion between the count of non-leaf nodes and the aggregate count of nodes in a fully balanced K-ary tree of depth N.

    Args:
    k (int): The number of children for each non-leaf node.
    n (int): The depth of the K-ary tree.

    Returns:
    float: The proportion between the count of non-leaf nodes and the aggregate count of nodes.
    """
    total_nodes = (k ** (n + 1) - 1) // (k - 1)
    non_leaf_nodes = total_nodes - k ** n
    return non_leaf_nodes / total_nodes