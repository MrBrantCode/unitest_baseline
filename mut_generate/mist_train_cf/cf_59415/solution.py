"""
QUESTION:
Write a function `diameter(node)` to calculate the diameter of a binary tree given the root node. The diameter is defined as the length of the longest path between any two nodes in the tree. Assume the binary tree node structure is defined in the `Node` class where each node has a value and references to its left and right children. The function should return the diameter of the binary tree.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

def diameter_of_binary_tree(node):
    if node is None:
        return 0
    
    l_height = height(node.left)
    r_height = height(node.right)
    
    l_diameter = diameter_of_binary_tree(node.left)
    r_diameter = diameter_of_binary_tree(node.right)
    
    return max(l_height + r_height + 1, max(l_diameter, r_diameter))