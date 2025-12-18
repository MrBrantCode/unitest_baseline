"""
QUESTION:
Implement a function to construct a Binary Search Tree (BST) with order-sensitive insertion, and include methods to display the tree (in-order, pre-order, post-order), calculate the height of the tree, and verify if the tree is a valid BST.

The `insert` function should take a `root` node and a new `node` as input, and return the updated `root` node. The `root` node should be updated based on the value of the new `node` and the order of insertion.

The `print_in_order`, `print_pre_order`, and `print_post_order` functions should take a `root` node as input and print the values of the nodes in the respective order.

The `tree_height` function should take a `root` node as input and return the height of the tree.

The `is_valid_BST` function should take a `root` node as input and return `True` if the tree is a valid BST and `False` otherwise.
"""

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def construct_bst(root, node):
    if root is None:
        return node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                root.right = construct_bst(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                root.left = construct_bst(root.left, node)
    return root

def print_in_order(root):
    if root:
        print_in_order(root.left)
        print(root.data)
        print_in_order(root.right)

def print_pre_order(root):
    if root:
        print(root.data)
        print_pre_order(root.left)
        print_pre_order(root.right)

def print_post_order(root):
    if root:
        print_post_order(root.left)
        print_post_order(root.right)
        print(root.data)

def tree_height(root):
    if root is None:
        return 0
    else:
        return max(tree_height(root.left), tree_height(root.right)) + 1

def is_valid_BST(root, left=None, right=None):
    if root is None:
        return True
    if left is not None and root.data <= left.data:
        return False
    if right is not None and root.data >= right.data:
        return False

    return is_valid_BST(root.left, left, root) and is_valid_BST(root.right, root, right)