"""
QUESTION:
Create a function named `is_balanced_and_inorder_traversal` that takes the root of a binary tree as input and returns True if the tree is balanced and False otherwise. The tree is considered balanced if the heights of its left and right subtrees differ by no more than 1. The function should also print all the nodes in the tree in inorder traversal order.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced_and_inorder_traversal(root):
    def height(node):
        if node is None:
            return 0
        return 1 + max(height(node.left), height(node.right))

    def inorder(node):
        if node:
            inorder(node.left)
            print(node.val, end=" ")
            inorder(node.right)

    if root is None:
        return True

    inorder(root)

    return abs(height(root.left) - height(root.right)) <= 1 and is_balanced_and_inorder_traversal(root.left) and is_balanced_and_inorder_traversal(root.right)