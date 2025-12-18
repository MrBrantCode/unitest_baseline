"""
QUESTION:
Calculate the proportion of nonterminal nodes to total nodes in a fully developed K-ary tree of depth N. The function should be able to estimate this proportion based on the given parameters K and N. The proportion should be calculated as the number of nonterminal nodes divided by the total number of nodes.
"""

def proportion_nonterminal_nodes(k, n):
    """
    Calculate the proportion of nonterminal nodes to total nodes in a fully developed K-ary tree of depth N.

    Args:
        k (int): The number of children each node has in the K-ary tree.
        n (int): The depth of the K-ary tree.

    Returns:
        float: The proportion of nonterminal nodes to total nodes.
    """
    return ((k**n) - 1) / ((k**(n+1)) - 1)