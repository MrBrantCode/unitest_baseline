"""
QUESTION:
Find the mode in a B-tree with a time complexity of O(log n), where n is the total number of nodes. The function, `find_mode`, should take the root of the B-tree as input and return the mode value. The function should handle edge cases, including an empty tree, a tree with all unique values, and a tree with all values being the same.
"""

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_mode(root):
    """
    Finds the mode in a B-tree.

    Args:
    root: The root of the B-tree.

    Returns:
    The mode value in the B-tree.
    """
    if not root:
        return None  # handle empty tree

    frequency_map = {}
    max_frequency = 0
    mode = None

    def in_order_traversal(node):
        nonlocal max_frequency, mode
        if node:
            in_order_traversal(node.left)
            frequency_map[node.value] = frequency_map.get(node.value, 0) + 1
            if frequency_map[node.value] > max_frequency:
                max_frequency = frequency_map[node.value]
                mode = node.value
            in_order_traversal(node.right)

    in_order_traversal(root)
    return mode