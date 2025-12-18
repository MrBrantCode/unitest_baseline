"""
QUESTION:
Design an iterative function called `isValidBST` that takes the root of a binary tree as input and returns a boolean value indicating whether the binary tree is a valid Binary Search Tree (BST). The function should have a time complexity of O(n) and a space complexity of O(h), where n is the number of nodes in the tree and h is the height of the tree, without using recursion or any extra data structures.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    stack = []
    prev = None
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        if prev and current.val <= prev.val:
            return False

        prev = current
        current = current.right

    return True