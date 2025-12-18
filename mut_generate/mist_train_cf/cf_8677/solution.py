"""
QUESTION:
Design a function called `insert` that inserts nodes into a binary search tree and calculates the product of all values in the left and right subtrees for each node. The tree should maintain the property that the left child of a node has a value less than its parent and the right child has a value greater than its parent. The function should take two parameters: `root` (the current root node) and `value` (the value to be inserted). The function should return the updated root node.

The `insert` function should be part of a class-based implementation of a binary tree node, where each node has attributes for its value, left child, right child, product of values in the left subtree, and product of values in the right subtree.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.left_product = 1
        self.right_product = 1

def insert(root, value):
    if root is None:
        return Node(value)
    elif value < root.value:
        root.left = insert(root.left, value)
        if root.left.left is None and root.left.right is None:
            root.left_product = root.left.value
        else:
            root.left_product = root.left.left_product * root.left.value * root.left.right_product
    elif value > root.value:
        root.right = insert(root.right, value)
        if root.right.left is None and root.right.right is None:
            root.right_product = root.right.value
        else:
            root.right_product = root.right.left_product * root.right.value * root.right.right_product
    return root