"""
QUESTION:
Write a function named `is_balanced` that checks if a binary tree is balanced. The function should return True if the tree is balanced and False otherwise. A binary tree is considered balanced if the heights of its left and right subtrees differ by no more than 1. 

The function should also perform an inorder traversal of the binary tree and calculate the frequency of each node using only the existing tree structure. 

The function should have a time complexity of O(n), where n is the number of nodes in the tree.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root):
    def height(node):
        if node is None:
            return 0
        return max(height(node.left), height(node.right)) + 1

    def inorder(node, freq):
        if node is None:
            return

        inorder(node.left, freq)
        freq[node.val] = freq.get(node.val, 0) + 1
        inorder(node.right, freq)

    freq = {}
    inorder(root, freq)

    if root is None:
        return True

    left_height = height(root.left)
    right_height = height(root.right)

    return abs(left_height - right_height) <= 1