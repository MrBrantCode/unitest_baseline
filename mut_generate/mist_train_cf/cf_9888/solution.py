"""
QUESTION:
Write a function `findGreaterValues` that takes the root of a binary search tree (BST) as input. The function should return a list where each element represents the number of values greater than the corresponding node in the BST. The order of elements in the output list should match the order of nodes in an in-order traversal of the BST.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findGreaterValues(root):
    count = 0
    result = []
    
    def inorderTraversal(node):
        nonlocal count
        if node:
            inorderTraversal(node.left)
            count += 1
            result.append(count)
            inorderTraversal(node.right)
    
    inorderTraversal(root)
    return result