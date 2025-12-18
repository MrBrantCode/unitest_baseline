"""
QUESTION:
Implement a function `sumBST(root)` that takes the root node of a binary tree as input and returns the sum of the values of all nodes in the tree, modulo `10^9+7`. The function should be implemented recursively and without using any additional data structures.
"""

def sumBST(root):
    if root is None:
        return 0

    left_sum = sumBST(root.left)
    right_sum = sumBST(root.right)
    current_sum = (left_sum + right_sum + root.val) % (10**9 + 7)

    return current_sum