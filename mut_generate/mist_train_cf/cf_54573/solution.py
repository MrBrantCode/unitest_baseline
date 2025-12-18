"""
QUESTION:
Write a function `diameter(node)` that calculates the diameter of a balanced binary tree, where the diameter is the longest path between any two nodes in the tree. The function takes the root node of the binary tree as input and returns the diameter of the tree. The binary tree is represented using nodes with a value and references to their left and right children.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def entance(node):
    if node is None:
        return 0

    left_height = height(node.left)
    right_height = height(node.right)

    left_diameter = entance(node.left)
    right_diameter = entance(node.right)

    return max(left_height + right_height + 1, max(left_diameter, right_diameter))

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))