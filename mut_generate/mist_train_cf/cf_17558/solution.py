"""
QUESTION:
Write a function `is_valid_bst` that takes the root of a binary tree as input and returns a tuple containing a boolean indicating whether the binary tree is a valid binary search tree (BST), the minimum value in the binary tree, the maximum value in the binary tree, and a boolean indicating whether the binary tree is balanced. The function should not use recursion or any built-in stack or queue data structures. The binary tree is balanced if the heights of the left and right subtrees of every node differ by at most one.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_valid_bst(root):
    stack = []
    prev = None
    min_value = float('inf')
    max_value = float('-inf')
    is_balanced = True

    def height(node):
        nonlocal is_balanced
        if node is None:
            return 0

        left_height = height(node.left)
        if left_height == -1:
            is_balanced = False
            return -1

        right_height = height(node.right)
        if right_height == -1:
            is_balanced = False
            return -1

        if abs(left_height - right_height) > 1:
            is_balanced = False
            return -1

        return max(left_height, right_height) + 1

    height(root)

    while stack or root:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()

        if prev and root.value <= prev.value:
            return False, min_value, max_value, False

        min_value = min(min_value, root.value)
        max_value = max(max_value, root.value)

        prev = root
        root = root.right

    return True, min_value, max_value, is_balanced