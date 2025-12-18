"""
QUESTION:
Given a sorted array of integers, implement a function `construct_avl_tree(arr)` that constructs a balanced AVL tree from the array and returns the root of the tree. The function should not use any built-in functions or libraries for AVL tree implementation.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


def construct_avl_tree(arr):
    if not arr:
        return None

    mid = len(arr) // 2
    root = TreeNode(arr[mid])

    root.left = construct_avl_tree(arr[:mid])
    root.right = construct_avl_tree(arr[mid + 1:])

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    return root


def get_height(node):
    if node is None:
        return 0
    return node.height