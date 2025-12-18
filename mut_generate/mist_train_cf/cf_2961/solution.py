"""
QUESTION:
Implement the `post_order_traversal` function to print out the value of each node in a given binary search tree. The binary search tree is represented as a linked data structure where each node contains a value and references to its left and right children. The `post_order_traversal` function should take a `node` as input and perform a post-order traversal of the binary search tree, printing the value of each node in the correct order.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def post_order_traversal(node):
    if node is None:
        return
    
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    
    print(node.value)