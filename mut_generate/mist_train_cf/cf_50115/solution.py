"""
QUESTION:
Create a function named `count_terminal_nodes` that takes the root of a trinary tree as input and returns the quantity of terminal (leaf) nodes in the tree. The tree is represented as a node with a value and three children, each child being another node or None if there is no child.
"""

class Node:
    def __init__(self, val=None, left=None, middle=None, right=None):
        self.val = val
        self.left = left
        self.middle = middle
        self.right = right

def count_terminal_nodes(root):
    if root is None: return 0
    if root.left is None and root.middle is None and root.right is None: return 1
    return count_terminal_nodes(root.left) + count_terminal_nodes(root.middle) + count_terminal_nodes(root.right)