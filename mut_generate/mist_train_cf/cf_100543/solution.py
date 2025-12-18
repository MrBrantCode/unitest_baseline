"""
QUESTION:
Implement a Python function `insertIntoBST(root, val)` that inserts a given value `val` at the appropriate position in a binary search tree represented by its root node `root`. The function should return the root node of the modified binary search tree. The function should use a `TreeNode` class to represent each node in the binary search tree, where each node has a `val` attribute to store its value, and `left` and `right` attributes to store its left and right child nodes, respectively.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insertIntoBST(root, val):
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)
        
    return root