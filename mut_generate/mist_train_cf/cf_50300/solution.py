"""
QUESTION:
Implement a function, `get_diameter`, that calculates the diameter of a balanced binary tree. The function should take the root node of the binary tree as input and return the length of the longest path between any two nodes. The function should be optimized for performance and able to handle large binary trees of up to 10^5 nodes. Note that the binary tree nodes hold any integer (positive or negative) and the tree may be modified externally while the function is executing.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def get_diameter(root):
    diameter = float('-inf')  

    def height_and_diameter(node):
        nonlocal diameter
        if node is None:
            return 0

        # recursively get the heights of left and right subtrees
        left_height = height_and_diameter(node.left)
        right_height = height_and_diameter(node.right)

        # update the diameter
        diameter = max(diameter, left_height + right_height)

        # return the height
        return 1 + max(left_height, right_height)

    height_and_diameter(root)
    return diameter