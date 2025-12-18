"""
QUESTION:
Implement the `findMaxElement` function that takes the root node of a Binary Search Tree (BST) as input and returns the maximum element in the tree. The function should not use recursion or any built-in functions or libraries. It should traverse the tree iteratively and update the maximum element as it moves through the nodes.
"""

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def findMaxElement(root):
    maxElement = float('-inf')  # Initialize maxElement to negative infinity
    current = root

    while current:
        if current.val > maxElement:
            maxElement = current.val
        
        if current.right:
            current = current.right
        else:
            current = current.left

    return maxElement