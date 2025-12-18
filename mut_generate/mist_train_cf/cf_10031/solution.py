"""
QUESTION:
Create a function named `is_balanced` that checks if a binary tree is balanced, where a binary tree is considered balanced if the heights of its left and right subtrees differ by no more than 1. The function should return `True` if the tree is balanced and `False` otherwise. The function should also print all the nodes in the tree in inorder traversal order.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root):
    if root is None:
        return True

    # Helper function to calculate the height of a node
    def height(node):
        if node is None:
            return 0
        return 1 + max(height(node.left), height(node.right))

    # Check if the heights of left and right subtrees differ by no more than 1
    if abs(height(root.left) - height(root.right)) > 1:
        return False

    # Recursively check if the left and right subtrees are balanced
    return is_balanced(root.left) and is_balanced(root.right)

    # Helper function to print the nodes in the tree in inorder traversal order
    def inorder(node):
        if node:
            inorder(node.left)
            print(node.val, end=" ")
            inorder(node.right)

    inorder(root)