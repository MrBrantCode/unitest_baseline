"""
QUESTION:
Create a function called `are_identical` that checks if two binary trees are identical in structure and have the same values in each corresponding node. The function should take two parameters `root1` and `root2` which are the roots of the two binary trees. It should return `True` if the trees are identical and `False` otherwise.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def are_identical(root1, root2):
    # If both trees are empty, they are identical
    if root1 is None and root2 is None:
        return True

    # If one tree is empty and the other is not, they are not identical
    if root1 is None or root2 is None:
        return False

    # Check if current nodes have the same value and recursively check left and right subtrees
    return (root1.value == root2.value and
            are_identical(root1.left, root2.left) and
            are_identical(root1.right, root2.right))