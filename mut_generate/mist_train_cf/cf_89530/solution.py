"""
QUESTION:
Write a function `post_order_traversal` that traverses a binary tree in post-order and returns the count and sum of nodes with values greater than a given value. The binary tree is not guaranteed to be a binary search tree, and the function should not assume any particular order of node values. The function should take two parameters: the root of the binary tree and the given value.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def post_order_traversal(root, given_value):
    count = 0
    total_sum = 0

    if root is None:
        return count, total_sum

    # Traverse left subtree
    count_left, sum_left = post_order_traversal(root.left, given_value)
    count += count_left
    total_sum += sum_left

    # Traverse right subtree
    count_right, sum_right = post_order_traversal(root.right, given_value)
    count += count_right
    total_sum += sum_right

    # Check the value of current node
    if root.value > given_value:
        count += 1
        total_sum += root.value

    return count, total_sum