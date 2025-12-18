"""
QUESTION:
Write a function `countGreaterValues` that takes in the root node of a Binary Search Tree (BST) and returns a list of integers representing the number of values greater than each node in the BST. The input BST can have duplicate values and will not be null.
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def countGreaterValues(root):
    result = []
    count = 0
    stack = []
    node = root

    while stack or node:
        while node:
            stack.append(node)
            node = node.right

        node = stack.pop()
        count += 1
        result.append(count)
        node = node.left

    return result