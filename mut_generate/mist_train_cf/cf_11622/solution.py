"""
QUESTION:
Write a function `tree_to_string(root)` that generates a string representation of a binary tree. The string representation should be generated in a depth-first manner, starting from the root node. Each node in the tree should be represented as a pair of parentheses containing the node's value. The left subtree should be represented within the parentheses of the node, followed by a hyphen ("-"), and then the right subtree represented within another set of parentheses. If a node has no left or right subtree, it should be represented with an empty set of parentheses "()". The function should handle empty trees and trees with any number of nodes.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_to_string(root):
    if root is None:
        return ""
    
    left_string = tree_to_string(root.left)
    right_string = tree_to_string(root.right)
    
    if left_string == "" and right_string == "":
        return f"{root.value}()"
    elif right_string == "":
        return f"{root.value}({left_string})-()"
    elif left_string == "":
        return f"{root.value}()-({right_string})"
    else:
        return f"{root.value}({left_string})-({right_string})"