"""
QUESTION:
Design a function `isValidBST` that checks if a given binary tree is a valid Binary Search Tree (BST) with a time complexity of O(n) and a space complexity of O(h), where n is the number of nodes in the tree and h is the height of the tree. The BST can contain duplicate values, and the function should not use any extra data structures or recursion. The function should keep track of the maximum and minimum values allowed for each node.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isValidBST(root):
    stack = []
    prev = float('-inf')
    
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        
        if root.val <= prev:
            return False
        prev = root.val
        root = root.right
    
    return True