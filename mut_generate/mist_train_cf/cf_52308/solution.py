"""
QUESTION:
Implement a function `findDuplicates(root)` that performs a preorder traversal of a binary tree and returns a list of duplicate values in the tree. The function should use a hash-based approach to track visited nodes and identify duplicates. The binary tree node is defined by a class `TreeNode` with attributes `val`, `left`, and `right`.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def findDuplicates(root):
    duplicates = set()
    visited = set()
    
    def preorder(node):
        if node:
            if node.val in visited:
                duplicates.add(node.val)
            else:
                visited.add(node.val)
            preorder(node.left)
            preorder(node.right)
    
    preorder(root)
    return list(duplicates)