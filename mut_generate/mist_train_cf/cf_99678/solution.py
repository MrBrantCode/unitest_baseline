"""
QUESTION:
Implement a function `insertIntoBST(root, val)` that inserts a given value into a binary search tree at the appropriate position. The function should take in the root node of the binary search tree and the value to be inserted as arguments, and return the root node of the modified binary search tree. The binary search tree is represented using a TreeNode class where each node has a value and references to its left and right child nodes.
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