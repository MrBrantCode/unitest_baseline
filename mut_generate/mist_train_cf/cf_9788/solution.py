"""
QUESTION:
Write a function, print_preorder_traversal_and_get_tree_info, that performs a pre-order traversal of a binary tree, prints the node values in pre-order, counts the number of nodes in the tree, and calculates the sum of all the node values. The function should take the root node of the tree as input and return the count and sum of node values. The space complexity of the solution should be O(1).
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_preorder_traversal_and_get_tree_info(root):
    """
    Performs a pre-order traversal of a binary tree, prints the node values in pre-order, 
    counts the number of nodes in the tree, and calculates the sum of all the node values.

    Args:
    root (Node): The root node of the binary tree.

    Returns:
    tuple: A tuple containing the count and sum of node values.
    """
    if root is None:
        return 0, 0

    # Pre-order traversal: Root -> Left -> Right
    print(root.value, end=" ")
    left_count, left_sum = print_preorder_traversal_and_get_tree_info(root.left)
    right_count, right_sum = print_preorder_traversal_and_get_tree_info(root.right)

    # Calculate the total count and sum
    total_count = 1 + left_count + right_count
    total_sum = root.value + left_sum + right_sum

    return total_count, total_sum