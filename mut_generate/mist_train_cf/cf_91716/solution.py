"""
QUESTION:
Define a function `isValidBST` that checks if a given binary tree is a valid Binary Search Tree (BST), keeping track of the maximum and minimum values allowed for each node. The function should take a binary tree node and its minimum and maximum allowed values as input and return a boolean indicating whether the subtree rooted at the node is a valid BST. The function should handle the case where the input node is None.
"""

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def isValidBST(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True
    
    if node.value < min_val or node.value >= max_val:
        return False
    
    return (isValidBST(node.left, min_val, node.value) and 
            isValidBST(node.right, node.value, max_val))