"""
QUESTION:
Given a non-null root node of a Binary Search Tree (BST), write a function `countGreaterValues` that returns a list of integers representing the number of values greater than each node in the BST. The BST can have duplicate values. The function should traverse the tree and for each node, count the number of values greater than it.
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