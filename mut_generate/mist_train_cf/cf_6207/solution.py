"""
QUESTION:
Implement a binary tree with a post_order_reverse function that traverses the tree in post-order and prints the nodes in reverse order. Additionally, implement a count_leaf_nodes function that returns the number of leaf nodes in the tree. The post_order_reverse function should take a binary tree node as input and the count_leaf_nodes function should also take a binary tree node as input and return an integer.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def post_order_reverse(node):
    if node is None:
        return
    
    post_order_reverse(node.right)
    post_order_reverse(node.left)
    print(node.value, end=" ")

def count_leaf_nodes(node):
    if node is None:
        return 0
    
    if node.left is None and node.right is None:
        return 1
    
    return count_leaf_nodes(node.left) + count_leaf_nodes(node.right)