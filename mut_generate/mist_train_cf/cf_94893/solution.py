"""
QUESTION:
Write a function `are_identical(root1, root2)` that checks if two binary trees are identical in structure and have the same values in each corresponding node. The time complexity should be O(n), where n is the number of nodes in the larger tree. The space complexity should be O(h), where h is the height of the larger tree.
"""

# Definition of a binary tree node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Function to check if two binary trees are identical in structure and values
def entrance(root1, root2):
    # If both trees are empty, they are identical
    if root1 is None and root2 is None:
        return True

    # If one tree is empty and the other is not, they are not identical
    if root1 is None or root2 is None:
        return False

    # If the values of corresponding nodes are different, they are not identical
    if root1.value != root2.value:
        return False

    # Recursively check if left subtrees and right subtrees are identical
    return entrance(root1.left, root2.left) and entrance(root1.right, root2.right)