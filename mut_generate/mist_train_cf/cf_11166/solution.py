"""
QUESTION:
Design a function `isValidBST(node, min_val, max_val)` that checks if a given binary tree rooted at `node` is a valid Binary Search Tree (BST), considering the given `min_val` and `max_val` as the allowed range of values for the node. The function should return `True` if the tree is a valid BST and `False` otherwise. The function should handle empty trees and trees with a single node.
"""

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def entance(node, min_val, max_val):
    if node is None:
        return True
    
    if node.value < min_val or node.value >= max_val:
        return False
    
    if not entance(node.left, min_val, node.value):
        return False
    
    if not entance(node.right, node.value, max_val):
        return False
    
    return True