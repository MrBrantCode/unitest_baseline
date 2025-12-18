"""
QUESTION:
Write a function named `diameter` to compute the diameter of a binary tree. The function should take the root of the tree as input and return the length of the longest path between any two nodes in the tree. The path may or may not pass through the root. Assume the tree nodes have a `value`, `left` child, `right` child, and a `height` property.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

def diameter(root):
    if not root:
        return 0

    left_height = root.height if root.left else 0
    right_height = root.height if root.right else 0

    left_diameter = diameter(root.left)
    right_diameter = diameter(root.right)

    return max(left_height + right_height + 1, max(left_diameter, right_diameter))