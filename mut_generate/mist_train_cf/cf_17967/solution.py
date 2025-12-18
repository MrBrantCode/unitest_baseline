"""
QUESTION:
Implement a function named `find_min_max` that uses a binary search tree data structure to find the minimum and maximum element from a collection of numbers with a time complexity of O(log n) without using any built-in data structures or libraries. The function should be able to insert numbers into the tree and then find the minimum and maximum values.
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return TreeNode(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

def find_min_max(root):
    min_val = [root.data]
    max_val = [root.data]

    def find_min(node):
        if node.left is None:
            min_val[0] = node.data
            return
        find_min(node.left)

    def find_max(node):
        if node.right is None:
            max_val[0] = node.data
            return
        find_max(node.right)

    find_min(root)
    find_max(root)

    return min_val[0], max_val[0]