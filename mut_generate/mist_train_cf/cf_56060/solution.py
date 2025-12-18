"""
QUESTION:
Write a function `diameter` that calculates the diameter of a binary tree. The diameter is defined as the longest distance between any two nodes. The function should take the root of the binary tree as an argument and return the diameter of the tree. Assume that the height of an empty tree is 0. The function should also consider the potential impact of the tree's balance on the diameter and the implications of different node arrangements.
"""

class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

def diameter(root):
    def height(node):
        if node is None:
            return 0, 0

        left_diameter, left_height = height(node.left)
        right_diameter, right_height = height(node.right)

        current_diameter = max(left_height + right_height + 1, max(left_diameter, right_diameter))
        current_height = max(left_height, right_height) + 1

        return current_diameter, current_height

    return height(root)[0]