"""
QUESTION:
Write a function `delete` that takes a binary search tree and a node value as input, deletes the node with the given value, and returns the number of leaf nodes left in the tree. Assume that the binary search tree property is maintained after the deletion.
"""

def delete(root, x):
    if not root:
        return root

    if root.key > x:
        root.left = delete(root.left, x)
    elif root.key < x:
        root.right = delete(root.right, x)
    else:
        if not root.right:
            return root.left
        elif not root.left:
            return root.right
        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root


def min_value_node(root):
    current = root
    while(current.left is not None):
        current = current.left
    return current


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    else:
        return count_leaves(node.left) + count_leaves(node.right)


def delete_and_count_leaves(root, x):
    root = delete(root, x)
    return count_leaves(root)