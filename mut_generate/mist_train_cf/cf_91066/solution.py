"""
QUESTION:
Write a function `print_preorder`, `count_nodes`, and `sum_nodes` for a binary tree. The function should print the binary tree in pre-order traversal, count the number of nodes in the tree, and find the sum of all the node values. The number of nodes in the tree can range from 1 to 10^6, and the value of each node can range from -10^6 to 10^6. The space complexity should be O(1), excluding the space needed for the recursive call stack.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_preorder(root):
    if root is None:
        return

    print(root.value, end=" ")
    print_preorder(root.left)
    print_preorder(root.right)

def count_nodes(root):
    if root is None:
        return 0

    return 1 + count_nodes(root.left) + count_nodes(root.right)

def sum_nodes(root):
    if root is None:
        return 0

    return root.value + sum_nodes(root.left) + sum_nodes(root.right)