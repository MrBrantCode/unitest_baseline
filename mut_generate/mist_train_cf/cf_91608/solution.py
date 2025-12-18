"""
QUESTION:
Create a function called `are_identical` that takes two binary tree roots (`root1` and `root2`) as input and returns `True` if the two binary trees are identical in structure and have the same values in each corresponding node, and `False` otherwise.
"""

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