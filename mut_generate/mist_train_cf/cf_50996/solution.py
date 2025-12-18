"""
QUESTION:
Implement a function called `pre_order_traversal(root)` that performs a depth-first search in a binary tree using pre-order traversal. The binary tree is represented with a node class that has 'value', 'left', and 'right' attributes. The function should process the root node first, followed by its left and right subtrees. Assume the input is a binary tree where each node has a unique 'value' and optional 'left' and 'right' child nodes. The function should not return any value but instead print the node values in the order they are visited.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def pre_order_traversal(root):
    if root is None:
        return
    
    print(root.value)
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)