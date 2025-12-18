"""
QUESTION:
Construct a function named `construct_avl_tree` that takes a sorted array of integers as input and returns the root of a balanced AVL tree. You cannot use any built-in functions or libraries for AVL tree implementation. The function should ensure that the constructed AVL tree is balanced, meaning the heights of the left and right subtrees of every node differ by at most 1.
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