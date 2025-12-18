"""
QUESTION:
Design a function `insert(root, value)` to insert a value into a binary search tree and update the product of all the values in its left subtree and the product of all the values in its right subtree for each node. The function should maintain the properties of a binary search tree, where the left child of a node should always have a value less than its parent, and the right child should always have a value greater than its parent. The initial tree is empty, and the values are inserted in a given order.
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
        root.left_product = root.left_product * value
    elif value > root.value:
        root.right = insert(root.right, value)
        root.right_product = root.right_product * value
    return root