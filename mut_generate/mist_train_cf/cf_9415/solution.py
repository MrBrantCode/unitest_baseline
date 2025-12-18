"""
QUESTION:
Implement a function named `post_order_sum` that takes the root of a binary tree as input and returns the sum of all the values in the tree. The binary tree is defined by a Node class with a value attribute and left and right child pointers. The function should use post-order traversal.
"""

def post_order_sum(root):
    if root is None:
        return 0

    left_sum = post_order_sum(root.left)
    right_sum = post_order_sum(root.right)

    return left_sum + right_sum + root.value