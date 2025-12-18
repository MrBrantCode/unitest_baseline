"""
QUESTION:
Implement a function `print_avl_tree_with_balance_factors` that takes the root of an AVL tree as input, prints the textual representation of the AVL tree with balance factors, and returns the total number of nodes in the tree. Each node in the AVL tree contains an integer value and a balance factor indicating the difference in height between its left and right subtree. The function should work for any valid AVL tree with unique node values.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.balance_factor = 0

def print_avl_tree_with_balance_factors(root):
    """
    Prints the textual representation of the AVL tree with balance factors and returns the total number of nodes.
    
    Args:
        root (Node): The root of the AVL tree.
    
    Returns:
        int: The total number of nodes in the tree.
    """
    def update_balance_factor(node):
        if not node:
            return 0
        left_height = get_height(node.left)
        right_height = get_height(node.right)
        node.balance_factor = right_height - left_height
        return node.balance_factor

    def get_height(node):
        if not node:
            return 0
        left_height = get_height(node.left)
        right_height = get_height(node.right)
        return max(left_height, right_height) + 1

    def print_tree(node):
        if node:
            print_tree(node.left)
            print(f"{node.data} ({node.balance_factor})")
            print_tree(node.right)

    def count_nodes(node):
        if not node:
            return 0
        return 1 + count_nodes(node.left) + count_nodes(node.right)

    update_balance_factor(root)
    print_tree(root)
    return count_nodes(root)