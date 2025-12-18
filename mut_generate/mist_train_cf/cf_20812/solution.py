"""
QUESTION:
Implement two functions, `pre_order_reverse(node)` and `count_nodes(node)`, for a binary tree represented by a Node class with a value and left and right child nodes. The `pre_order_reverse(node)` function should perform a pre-order traversal of the binary tree in reverse order, printing the node values in the reverse order they were visited. The `count_nodes(node)` function should return the total number of nodes in the binary tree.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def entrance(node):
    if node is None:
        return 0, []
    
    left_count, left_values = entrance(node.left)
    right_count, right_values = entrance(node.right)

    return 1 + left_count + right_count, [node.value] + right_values + left_values