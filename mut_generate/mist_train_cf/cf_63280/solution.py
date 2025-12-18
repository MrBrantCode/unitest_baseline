"""
QUESTION:
Write a function `calculate_tree_params(root)` that calculates the number of nodes, height, and diameter of a binary tree given its root node. The function should return a tuple containing the number of nodes, height, and diameter. The binary tree is represented by a custom `TreeNode` class with "left" and "right" children, and each node has a value. The function should have a time complexity of O(n), where n is the number of nodes in the tree.
"""

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def entance(root):
    if root is None:
        return (0, 0, 0)  # number of nodes, height, diameter

    left_nodes, left_height, left_diameter = entance(root.left)
    right_nodes, right_height, right_diameter = entance(root.right)

    num_nodes = 1 + left_nodes + right_nodes
    height = 1 + max(left_height, right_height)
    longest_path = left_height + right_height
    diameter = max(longest_path, left_diameter, right_diameter)

    return (num_nodes, height, diameter)