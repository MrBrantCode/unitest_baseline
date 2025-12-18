"""
QUESTION:
Design a function `median(Node *root)` that finds the median value in a self-balancing binary search tree (Red-Black tree), where each node contains the count of nodes in its left and right subtrees. The function should maintain an O(log n) time complexity, where n is the total number of nodes. The function should handle cases where the tree is empty or the median value is not unique (i.e., when the number of nodes is even).
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.left_count = 0
        self.right_count = 0
        self.color = None  # RED or BLACK


def find_median(root):
    """
    This function finds the median value in a self-balancing binary search tree (Red-Black tree).
    
    Parameters:
    root (Node): The root node of the Red-Black tree.
    
    Returns:
    Node: The node containing the median value.
    """
    if root is None:
        return None
    if root.left_count == root.right_count:
        return root
    elif root.left_count > root.right_count:
        return find_median(root.left)
    else:
        return find_median(root.right)