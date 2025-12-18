"""
QUESTION:
Implement a function `binary_tree_time_complexity` to explain the time complexity of a binary search tree. The function should describe the relationship between the number of elements in the tree and the time required to search the tree, expressed in Big O notation.
"""

def binary_tree_time_complexity(n):
    """
    Describes the time complexity of a binary search tree.

    The time complexity of a binary search tree is O(log n), where n is the number of elements in the tree.
    This is because in a binary search tree, each node can have up to two children, so the depth of the tree 
    is bounded by the logarithm of n. This means that the time required to search the tree is bounded by 
    the logarithm of n.

    Args:
        n (int): The number of elements in the tree.

    Returns:
        str: The time complexity of the binary search tree.
    """
    return "O(log n)"